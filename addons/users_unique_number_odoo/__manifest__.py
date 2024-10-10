# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt. Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "Unique Sequence Number of Users",
    'version': '4.1.3',
    'price': 12.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'category': 'Tools',
    'summary': """Internal Users and Portal Users Sequence Numbering""",
    'description': """
Users Unique Number Odoo
user number
user sequence number
user unique number
Users Unique Sequence Number Odoo
Internal Users Unique Number
Portal Users Unique Number

    """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.odoo.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/image.jpg'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/users_unique_number_odoo/452',#'https://youtu.be/wzDOzK-3PDs',
    'depends': ['base'],

    'data': [
        'data/user_sequence.xml',
        'views/res_users_view.xml',
    ],
    'installable': True,
    'application': False,
    
}
