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

class clv_cmed(osv.Model):
    _name = 'clv_cmed'

    def _compute_name(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            result[r.id] = '[' + str(r.codigo_ggrem) + '] ' + r.produto + ' ' + r.apresentacao + ' (' + r.principio_ativo + \
            	           ') ' + ' - ' + r.latoratorio + ' [' + r.ean + '] '
        return result

    _columns = {
        'name' : fields.function(_compute_name, method=True, type='char', size=256, string='CMED Description', store=True),
		# 'cod_prod': fields.integer(string='Cod Prod'),
		'principio_ativo': fields.char(size=128, string='Principio Ativo'),
		'cnpj': fields.char(size=128, string='CNPJ'),
		'latoratorio': fields.char(size=128, string='Laboratorio'),
		'codigo_ggrem': fields.char(size=13, string='Codigo GGREM'),
		'ean': fields.char(size=13, string='EAN'),
		'produto': fields.char(size=6, string='Produto'),
		'apresentacao': fields.char(size=128, string='Apresentacao'),
		'classe_terapeutica': fields.char(size=128, string='Classe Terapeutica'),
		'pf_0': fields.float(string='PF 0%'),
		'pf_12': fields.float(string='PF 12%'),
		'pf_17': fields.float(string='PF 17%'),
		'pf_18': fields.float(string='PF 18%'),
		'pf_19': fields.float(string='PF 19%'),
		'pf_17_zfm': fields.float(string='PF 17% ZONA FRANCA DE MANAUS'),
		'pmc_0': fields.float(string='PMC 0%'),
		'pmc_12': fields.float(string='PMC 12%'),
		'pmc_17': fields.float(string='PMC 17%'),
		'pmc_18': fields.float(string='PMC 18%'),
		'pmc_19': fields.float(string='PMC 19%'),
		'pmc_17_zfm': fields.float(string='PMC 17% ZONA FRANCA DE MANAUS'),
		'restr_hospitalar': fields.char(size=256, string='RESTRICAO_HOSPITALAR'),
		'cap': fields.char(size=256, string='CAP'),
		'confaz_87': fields.char(size=256, string='CONFAZ_87'),
		'analise_recursal': fields.char(size=256, string='ANALISE_RECURSAL'),

		'from': fields.char(size=128, string='From'),
		'excluded': fields.boolean('Excluded'),
		'product_name': fields.char(size=256, string='Product Name'),

        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the medicament without removing it."),
    }

    _order='name'

    # _sql_constraints = [('cod_prod_uniq', 'unique(cod_prod)', u'Duplicated CMED Code!')]

    _defaults = {
        'active': 1,
    }
