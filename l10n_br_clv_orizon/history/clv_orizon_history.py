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
from datetime import *

class clv_orizon_history(osv.osv):
    _name = 'clv_orizon.history'

    _order = "date desc"

    _columns = {
        'orizon_id': fields.many2one('clv_orizon', 'orizon', required=True, ondelete='cascade'),
        'user_id':fields.many2one ('res.users', 'User', required=True),
        'date': fields.datetime("Date", required=True),
        'state': fields.selection([('new','New'),
                                   ('revised','Revised'),
                                   ('waiting','Waiting'),
                                   ('done','Done'),
                                   ], string='Status', readonly=True, required=True, help=""),
        'notes': fields.text(string='Notes'),
        }
    
    _defaults = {
        'user_id': lambda self: self._uid,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'new',
        }

    _order = "date desc"

class clv_orizon(osv.osv):
    _inherit = 'clv_orizon'

    _columns = {
        'history_ids': fields.one2many('clv_orizon.history', 'orizon_id', 'Orizon History', readonly=True),
        'active_history': fields.boolean('Active History', 
                                         help="If unchecked, it will allow you to disable the history without removing it."),
        }
    
    _defaults = {
        'active_history': True
        }

    def insert_clv_orizon_history(self, cr, uid, active_history, orizon_id, state, notes, context=None):
        if context is None:
            context = {}
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if active_history:
            vals = { 
                'orizon_id': orizon_id,
                'user_id': uid,
                'date': date,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_orizon.history').create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if (not 'state' in vals) and (not 'date' in vals) and (not 'history_ids' in vals):
            notes = vals.keys()
            try:
                for orizon in self.browse(cr, uid, ids):
                    if 'active_history' in vals:
                        self.insert_clv_orizon_history(cr, uid, True, orizon.id, orizon.state, notes)
                    else:
                        self.insert_clv_orizon_history(cr, uid, orizon.active_history, orizon.id, orizon.state, notes)
            except:
                pass
        return super(clv_orizon, self).write(cr, uid, ids, vals, context)

    def button_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'new'})
        for orizon in self.browse(cr, uid, ids):
            self.insert_clv_orizon_history(cr, uid, orizon.active_history, orizon.id, 'new', '')

    def button_revised(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'revised'})
        for orizon in self.browse(cr, uid, ids):
            self.insert_clv_orizon_history(cr, uid, orizon.active_history, orizon.id, 'revised', '')

    def button_waiting(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'waiting'})
        for orizon in self.browse(cr, uid, ids):
            self.insert_clv_orizon_history(cr, uid, orizon.active_history, orizon.id, 'waiting', '')

    def button_done(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'done'})
        for orizon in self.browse(cr, uid, ids):
            self.insert_clv_orizon_history(cr, uid, orizon.active_history, orizon.id, 'done', '')
