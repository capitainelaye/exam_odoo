# -*- coding: utf-8 -*-
{
    'name': "Gestion des formations",

    'summary': """
        Ce module est destiné pour gérer un centre de formation
    """,

    'description': """
        Ce module est destiné pour gérer un centre de formation
    """,

    'author': "Abdoulaye Sow",
    'website': "http://www.https://www.odoo.com/fr_FR/my/home",
    
    # Categories can be used to filter modules in modules listing
    'category': 'Formations',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/gestion_formation.xml',
        'security/ir.model.access.csv'
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}