{
    'name': 'estate',
    'version': '1.0',
    'summary': 'Real estate management',
    'description': 'Module to manage real estate properties',
    'author': 'Your Name or Company',
    'category': 'Real Estate',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_type_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}