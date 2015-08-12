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

class clv_orizon(osv.Model):
    _name = 'clv_orizon'

    def _compute_name(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            result[r.id] = '[' + str(r.cod_prod) + '] ' + r.apres_produto + ' (' + r.principio_ativo + ') ' + ' - ' + \
                           r.latoratorio + ' [' + r.ean_principal + '] '
        return result

    _columns = {
        'name' : fields.function(_compute_name, method=True, type='char', size=256, string='Orizon Description', store=True),
		'cod_prod': fields.integer(string='Cod Prod'),
		'latoratorio': fields.char(size=128, string='Laboratorio'),
		'produto': fields.char(size=128, string='Produto'),
		'apres_produto': fields.char(size=128, string='Apresentacao Do Produto'),
		'ean_principal': fields.char(size=13, string='EAN Principal'),
		'ean_1': fields.char(size=13, string='EAN 1'),
		'ean_2': fields.char(size=13, string='EAN 2'),
		'ean_3': fields.char(size=13, string='EAN 3'),
		'pmc': fields.float(string='PMC[R$]'),
		'desconto': fields.float(string='Desconto[%]'),
		'preco_venda': fields.float(string='Preco Venda[R$]'),
		'categoria': fields.char(size=128, string='Categoria'),
		'sub_categoria': fields.char(size=128, string='Sub-Categoria'),
		'classificacao': fields.char(size=128, string='Classificacao'),
		'sub_classificacao': fields.char(size=128, string='Sub-Classificacao'),
		'descricao': fields.char(size=128, string='Descricao'),
		'classe_terapeutica': fields.char(size=128, string='Classe Terapeutica'),
		'sub_classe_terapeutica': fields.char(size=128, string='Sub-Classe Terapeutica'),
		'principio_ativo': fields.char(size=128, string='Principio Ativo'),

		'from': fields.char(size=128, string='From'),
		'excluded': fields.boolean('Excluded'),
		'product_name': fields.char(size=256, string='Product Name'),
        'is_fraction': fields.boolean('Is a Fraction', 
                                      help="Check if the medicament is a fraction of a product."),

        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the medicament without removing it."),
    }

    _order='name'

    _sql_constraints = [('cod_prod_uniq', 'unique(cod_prod)', u'Duplicated Orizon Code!')]

    _defaults = {
        'active': 1,
    }
