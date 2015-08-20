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

class clv_medicament_price_list_item(models.Model):
    _inherit = 'clv_medicament_price_list.item'

    consumer_price_12 = fields.Float('Consumer Price (12)')
    production_price_12 = fields.Float('Production Price (12)')
    consumer_price_17 = fields.Float('Consumer Price (17)')
    production_price_17 = fields.Float('Production Price (17)')
    consumer_price_18 = fields.Float('Consumer Price (18)')
    production_price_18 = fields.Float('Production Price (18)')
    consumer_price_19 = fields.Float('Consumer Price (19)')
    production_price_19 = fields.Float('Production Price (19)')
