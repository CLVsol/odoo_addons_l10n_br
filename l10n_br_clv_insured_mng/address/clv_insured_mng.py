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

class clv_insured_mng(models.Model):
    _inherit = 'clv_insured_mng'

    addr_l10n_br_city_id = fields.Many2one('l10n_br_base.city', u'Município', 
                                           domain="[('state_id','=',addr_state_id)]")
    addr_district = fields.Char('Bairro', size=32)
    addr_number = fields.Char(u'Número', size=10)

    @api.onchange('addr_l10n_br_city_id')
    def onchange_addr_l10n_br_city_id(self):
        """ Ao alterar o campo addr_l10n_br_city_id que é um campo relacional
        com o l10n_br_base.city que são os municípios do IBGE, copia o nome
        do município para o campo city que é o campo nativo do módulo base
        para manter a compatibilidade entre os demais módulos que usam o
        campo city.

        param int addr_l10n_br_city_id: id do addr_l10n_br_city_id digitado.

        return: dicionário com o nome e id do município.
        """
        if self.addr_l10n_br_city_id:
            self.addr_city = self.addr_l10n_br_city_id.name
            self.addr_l10n_br_city_id = self.addr_l10n_br_city_id

    @api.onchange('addr_zip')
    def onchange_mask_addr_zip(self):
        if self.addr_zip:
            val = re.sub('[^0-9]', '', self.addr_zip)
            if len(val) == 8:
                addr_zip = "%s-%s" % (val[0:5], val[5:8])
                self.addr_zip = addr_zip

    def addr_zip_search(self, cr, uid, ids, context=None):
        obj_addr_zip = self.pool.get('l10n_br.zip')
        for clv_insured_mng in self.browse(cr, uid, ids):
            addr_zip_ids = obj_addr_zip.zip_search_multi(
                cr, uid, ids, context,
                country_id=clv_insured_mng.addr_country_id.id,
                state_id=clv_insured_mng.addr_state_id.id,
                l10n_br_city_id=clv_insured_mng.addr_l10n_br_city_id.id,
                district=clv_insured_mng.addr_district,
                street=clv_insured_mng.addr_street,
                zip_code=clv_insured_mng.addr_zip,
            )

            addr_zip_data = obj_addr_zip.read(cr, uid, addr_zip_ids, False, context)
            obj_addr_zip_result = self.pool.get('l10n_br.zip.result')
            addr_zip_ids = obj_addr_zip_result.map_to_zip_result(
                cr, uid, 0, context, addr_zip_data, self._name, ids[0])

            if len(addr_zip_ids) == 1:  # FIXME
                result = obj_addr_zip.set_result(cr, uid, ids, context, addr_zip_data[0])
                addr_result = {
                    'addr_street':result['street'], 
                    'addr_district':result['district'],
                    'addr_zip':result['zip'],
                    'addr_country_id':result['country_id'],
                    'addr_l10n_br_city_id':result['l10n_br_city_id'],
                    'addr_state_id':result['state_id'],
                    }
                self.write(cr, uid, [clv_insured_mng.id], addr_result, context)
                return True
            else:
                if len(addr_zip_ids) > 1:
                    return obj_addr_zip.create_wizard(
                        cr, uid, ids, context, self._name,
                        country_id=clv_insured_mng.addr_country_id.id,
                        state_id=clv_insured_mng.addr_state_id.id,
                        l10n_br_city_id=clv_insured_mng.addr_l10n_br_city_id.id,
                        district=clv_insured_mng.addr_district,
                        street=clv_insured_mng.addr_street,
                        zip_code=clv_insured_mng.addr_zip,
                        zip_ids=addr_zip_ids
                    )
                else:
                    return True
