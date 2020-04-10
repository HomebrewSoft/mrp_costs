# -*- coding: utf-8 -*-
{
    'name': 'MRP Costs',
    'version': '0.3.0',
    'author': 'HomebrewSoft',
    'website': 'https://github.com/HomebrewSoft/mrp_costs',
    'depends': [
        'mrp',
        'purchase',
        'stock',
    ],
    'data': [
        # views
        'views/mrp_bom.xml',
        'views/mrp_production.xml',
        'views/product_template.xml',
        'views/mrp_costs_wizard.xml',
        'views/mrp_config.xml',
        'views/mrp_routing.xml',
    ],
}
