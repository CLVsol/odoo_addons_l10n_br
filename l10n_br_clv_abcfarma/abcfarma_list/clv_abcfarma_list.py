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

class clv_abcfarma_list(models.Model):
    _name = 'clv_abcfarma.list'

    name = fields.Char('List', required=True, size=64)
    code = fields.Char ('List Code',size=128, required=False)
    description = fields.Char(string='Description', size=256)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active', 
                            help='The active field allows you to hide the list without removing it.',
                            default=1)

    _sql_constraints = [
        ('uniq_list_name', 'unique(name)', "Error! The List Name must be unique!"),
        ('uniq_list_code', 'unique(code)', "Error! The List Code must be unique!"),
        ]
