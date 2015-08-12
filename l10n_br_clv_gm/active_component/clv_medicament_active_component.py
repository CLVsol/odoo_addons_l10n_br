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

from openerp.osv import fields, osv


class clv_medicament_active_component(osv.osv):
    _inherit = 'clv_medicament.active_component'

    _columns = {
        'gm_ids': fields.one2many('clv_gm', 'active_component', 'Orizon'),

        }

class clv_gm(osv.osv):
    _inherit = 'clv_gm'

    _columns = {
        'active_component': fields.many2one('clv_medicament.active_component', 
                                            string='Active Component', 
                                            help='Medicament Active Component'),
        'concentration': fields.char(size=256, string='Concentration'),
        'pres_form': fields.many2one('clv_medicament.form', string='Presentation Form', 
                                     help='Medicament form, such as tablet or gel'),
        'pres_form_2': fields.many2one('clv_medicament.form', string='Presentation Form 2', 
                                        help='Medicament form, such as tablet or gel'),
        'pres_quantity': fields.float(string='Presentation Quantity'),
        'pres_quantity_unit': fields.many2one('clv_medicament.uom', string='Quantity Unit', 
                                              help='Unit of measure for the medicament to be taken'),
        }
