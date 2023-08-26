{
    'name': "Developers Management",

    'summary': """
        Module for managing developers""",

    'author': "Vadim Mudruk",
    'website': "https://t.me/vadim_m23",

    'category': 'Uncategorized',
    'version': '16.0.1.0.1',
    'license': 'GPL-3',

    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/developers_management_developer_views.xml',
        'views/developers_management_company_views.xml',
        'views/menu_view.xml',
        'wizard/add_developer_wizard.xml',

    ],
}
