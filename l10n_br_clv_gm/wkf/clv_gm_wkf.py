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

class clv_gm(osv.osv):
    _inherit = 'clv_gm'

    _columns = {
        'state': fields.selection([('new','New'),
                                   ('revised','Revised'),
                                   ('waiting','Waiting'),
                                   ('done','Done'),
                                   ], string='Status', readonly=True, required=True, help=""),
        }
    
    _defaults = {
        'state': 'new',
        }

    def button_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'new'})

    def button_revised(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'revised'})

    def button_waiting(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'waiting'})

    def button_done(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'done'})
