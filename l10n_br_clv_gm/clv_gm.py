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

from openerp import tools, api
from openerp.osv import osv, fields

class clv_gm(osv.Model):
    _name = 'clv_gm'

    def _compute_name(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            result[r.id] = '[' + str(r.cod_prod_fabricante) + '] ' + r.nome_produto + ' (' + r.principio_ativo + ') ' + \
                           r.apresentacao + ' - ' + r.laboratorio
        return result

    _columns = {
        'name' : fields.function(_compute_name, method=True, type='char', size=256, string='GaranteMed Description', store=True),
		'cod_prod_fabricante': fields.integer(string='CodProdFabricante'),
		'cod_abcfarma': fields.char(size=128, string='CodABCFarma'),
		'nome_produto': fields.char(size=128, string='NomeProduto'),
		'apresentacao': fields.char(size=128, string='Apresentacao'),
		'laboratorio': fields.char(size=128, string='LABORATORIO'),
		'pco_consumidor_sp': fields.float(string='PCO CONSUMIDOR SP'),
		'pco_reposicao_sp': fields.float(string='PCO REPOSIÇÃO SP'),
		'principio_ativo': fields.char(size=128, string='PRINCIPIO ATIVO'),
		'status': fields.char(size=128, string='STATUS'),

		'from': fields.char(size=128, string='From'),
		'excluded': fields.boolean('Excluded'),
		'product_name': fields.char(size=256, string='Product Name'),
        'is_fraction': fields.boolean('Is a Fraction', 
                                      help="Check if the medicament is a fraction of a product."),

        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the medicament without removing it."),
    }

    _order='name'

    _sql_constraints = [('cod_prod_fabricante_uniq', 'unique(cod_prod_fabricante)', u'Error! Duplicated GaranteMed Code!')]

    _defaults = {
        'active': 1,
    }
