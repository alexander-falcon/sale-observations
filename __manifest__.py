# -*- coding: utf-8 -*-

{
    'name': "Sale Order Observations",
    'version': '16.0.1.0',
    'category': 'Sales',
    'description': 'Agrega un campo de observaciones a los pedidos de venta',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'application': False,
    'author': "Alexander Falcon",
    # 'website': "http://www.yourcompany.com",
    'license': 'LGPL-3',
}
