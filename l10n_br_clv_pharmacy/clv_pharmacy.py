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
from openerp.exceptions import Warning

def validate_cnpj(cnpj):

    if not cnpj.isdigit():
        cnpj = re.sub('[^0-9]', '', cnpj)
    if len(cnpj) != 14:
        return False
    cnpj = map(int, cnpj)
    new = cnpj[:12]
    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(new) < 14:
        r = sum([x * y for (x, y) in zip(new, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        new.append(f)
        prod.insert(0, 6)
    if new == cnpj:
        return True
    return False

class clv_pharmacy(models.Model):
    _inherit = 'clv_pharmacy'

    cnpj = fields.Char('CNPJ', size=18)
    legal_name = fields.Char(u'Razão Social', size=128, help="nome utilizado em documentos fiscais")

    _sql_constraints = [('cnpj_uniq', 'unique(cnpj)', u'Error! The CNPJ must be unique!')]

    @api.one
    @api.constrains('cnpj')
    def _check_cnpj(self):
        if self.cnpj:
            if not validate_cnpj(self.cnpj):
                raise Warning((u'CNPJ inválido!'))
        return True

    @api.onchange('cnpj')
    def onchange_mask_cnpj(self):
        if self.cnpj:
            val = re.sub('[^0-9]', '', self.cnpj)
            if len(val) == 14:
                cnpj = "%s.%s.%s/%s-%s" % (val[0:2], val[2:5], val[5:8], val[8:12], val[12:14])
                self.cnpj = cnpj
                if not validate_cnpj(self.cnpj):
                    raise Warning((u'CNPJ inválido!'))
            else:
                raise Warning((u'Verifique o CNPJ!'))
