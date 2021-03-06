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

{
    'name': 'ABCFARMA',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
ABCFARMA
========
    ''',
    'images': [],
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        'clv_medicament',
        'clv_medicament_mng',
        'l10n_br_clv_cmed',
        ],
    'data': [
        'security/ir.model.access.csv',
        'clv_abcfarma_view.xml',
        'clv_tag/clv_tag_view.xml',
        'clv_annotation/clv_annotation_view.xml',
        'wkf/clv_abcfarma_workflow.xml',
        'wkf/clv_abcfarma_wkf_view.xml',
        'history/clv_abcfarma_history_view.xml',
        'clv_medicament/clv_medicament_view.xml',
        'clv_medicament_mng/clv_medicament_mng_view.xml',
        'active_component/clv_medicament_active_component_view.xml',
        'manufacturer/clv_medicament_manufacturer_view.xml',
        'clv_cmed/clv_cmed_view.xml',
        'abcfarma_list/clv_abcfarma_list_view.xml',
        'abcfarma_list/clv_abcfarma_list_item_view.xml',
        'menu/clv_abcfarma_menu_view.xml',
        ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'active': False,
    'css': [],
}
