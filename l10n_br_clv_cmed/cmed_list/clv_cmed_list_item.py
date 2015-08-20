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

from openerp import models, fields, api

class clv_cmed_list_item(models.Model):
    _name = 'clv_cmed.list.item'

    list_id = fields.Many2one('clv_cmed.list', string='CMED List',
                              help='CMED List', required=False)
    medicament_id = fields.Many2one('clv_cmed', string='Medicament',
                                    help='CMED Medicament', required=False)
    notes = fields.Text(string='Notes')
    order = fields.Integer(string='Order',
                           default=10)
    pmc = fields.Float(string='PMC [R$]')
    desconto = fields.Float(string='Desconto [%]')
    preco_venda = fields.Float(string='Preço Venda [%]')
    included = fields.Boolean('Included')
    active = fields.Boolean('Active', 
                            help='The active field allows you to hide the list item without removing it.',
                            default=1)
    
    _order='order'

class clv_cmed_list(models.Model):
    _inherit = 'clv_cmed.list'

    cmed_list_item_ids = fields.One2many('clv_cmed.list.item',
                                               'list_id',
                                               'CMED List Itens')
