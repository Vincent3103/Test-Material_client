# -*- coding: utf-8 -*-
{
    'name': "Testing Material",

    'summary': """
        Module for handling Testing Material""",

    'description': """
        Module for handling Testing Material use
    """,

    'author': "Vincent Frandy",
    'website': "https://www.linkedin.com/in/vincent-frandy/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/testing_material.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}