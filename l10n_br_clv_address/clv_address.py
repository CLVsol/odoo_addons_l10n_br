# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

import re
from openerp import models, fields, api


class clv_address(models.Model):
    _inherit = 'clv_address'

    name = fields.Char(string="Name", store=True,
                       compute="_get_compute_name",
                       help='Use "/" to get an automatic new Address Name.')
    l10n_br_city_id = fields.Many2one('l10n_br_base.city', u'Município', domain="[('state_id','=',state_id)]")
    district = fields.Char('Bairro', size=32)
    number = fields.Char(u'Número', size=10)

    @api.model
    def _display_address(self, address, without_company=False):

        if address.country_id and address.country_id.code != 'BR':
            # this ensure other localizations could do what they want
            return super(clv_address, self)._display_address(
                address,
                without_company=False)
        else:
            address_format = (address.country_id and
                              address.country_id.address_format or
                              "%(street)s\n%(street2)s\n%(l10n_br_city_name)s %(state_code)s"
                              "%(zip)s\n%(country_name)s")
            args = {
                'state_code': address.state_id and address.state_id.code or '',
                'state_name': address.state_id and address.state_id.name or '',
                'country_code': address.country_id and
                address.country_id.code or '',
                'country_name': address.country_id and
                address.country_id.name or '',
                'l10n_br_city_name': address.l10n_br_city_id and
                address.l10n_br_city_id.name or '',
            }
            address_field = ['street', 'street2', 'zip', 'city',
                             'number', 'district']
            for field in address_field:
                args[field] = getattr(address, field) or ''
            return address_format % args

    @api.onchange('l10n_br_city_id')
    def onchange_l10n_br_city_id(self):
        """ Ao alterar o campo l10n_br_city_id que é um campo relacional
        com o l10n_br_base.city que são os municípios do IBGE, copia o nome
        do município para o campo city que é o campo nativo do módulo base
        para manter a compatibilidade entre os demais módulos que usam o
        campo city.

        param int l10n_br_city_id: id do l10n_br_city_id digitado.

        return: dicionário com o nome e id do município.
        """
        if self.l10n_br_city_id:
            self.city = self.l10n_br_city_id.name
            self.l10n_br_city_id = self.l10n_br_city_id

    @api.onchange('zip')
    def onchange_mask_zip(self):
        if self.zip:
            val = re.sub('[^0-9]', '', self.zip)
            if len(val) == 8:
                zip = "%s-%s" % (val[0:5], val[5:8])
                self.zip = zip

    @api.model
    def _address_fields(self):
        """ Returns the list of address fields that are synced from the parent
        when the `use_parent_address` flag is set.
        Extenção para os novos campos do endereço """
        address_fields = super(clv_address, self)._address_fields()
        return list(address_fields + ['l10n_br_city_id', 'number', 'district'])

    @api.onchange('l10n_br_city_id')
    def onchange_l10n_br_city_id(self):
        """ Ao alterar o campo l10n_br_city_id que é um campo relacional
        com o l10n_br_base.city que são os municípios do IBGE, copia o nome
        do município para o campo city que é o campo nativo do módulo base
        para manter a compatibilidade entre os demais módulos que usam o
        campo city.

        param int l10n_br_city_id: id do l10n_br_city_id digitado.

        return: dicionário com o nome e id do município.
        """
        if self.l10n_br_city_id:
            self.city = self.l10n_br_city_id.name
            self.l10n_br_city_id = self.l10n_br_city_id

    def zip_search(self, cr, uid, ids, context=None):
        obj_zip = self.pool.get('l10n_br.zip')
        for clv_address in self.browse(cr, uid, ids):
            zip_ids = obj_zip.zip_search_multi(
                cr, uid, ids, context,
                country_id=clv_address.country_id.id,
                state_id=clv_address.state_id.id,
                l10n_br_city_id=clv_address.l10n_br_city_id.id,
                district=clv_address.district,
                street=clv_address.street,
                zip_code=clv_address.zip,
            )

            zip_data = obj_zip.read(cr, uid, zip_ids, False, context)
            obj_zip_result = self.pool.get('l10n_br.zip.result')
            zip_ids = obj_zip_result.map_to_zip_result(
                cr, uid, 0, context, zip_data, self._name, ids[0])

            if len(zip_ids) == 1:  # FIXME
                result = obj_zip.set_result(cr, uid, ids, context, zip_data[0])
                self.write(cr, uid, [clv_address.id], result, context)
                return True
            else:
                if len(zip_ids) > 1:
                    return obj_zip.create_wizard(
                        cr, uid, ids, context, self._name,
                        country_id=clv_address.country_id.id,
                        state_id=clv_address.state_id.id,
                        l10n_br_city_id=clv_address.l10n_br_city_id.id,
                        district=clv_address.district,
                        street=clv_address.street,
                        zip_code=clv_address.zip,
                        zip_ids=zip_ids
                    )
                else:
                    return True

    @api.depends('street', 'number', 'street2')
    def _get_compute_name(self):
        if self.street:
            self.name = self.street
            if self.number:
                self.name = self.name + ', ' + self.number
                if self.street2:
                    self.name = self.name + ' - ' + self.street2
            else:
                if self.street2:
                    self.name = self.name + ' - ' + self.street2
        else:
            self.name = False

    @api.onchange('name')
    def onchange_name(self):
        if self.name == '/':
            if self.street:
                self.name = self.street
                if self.number:
                    self.name = self.name + ', ' + self.number
                    if self.street2:
                        self.name = self.name + ' - ' + self.street2
                else:
                    if self.street2:
                        self.name = self.name + ' - ' + self.street2
            else:
                self.name = False
