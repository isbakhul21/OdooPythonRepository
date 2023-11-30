{
    "name": "[Custom] Purchase",
    "summary": "Responsive web client, community-supported",
    "description": "This module contains all the common features of Purchase.",
    "version": "1.0.0",
    "category": "Purchase",
    "license": "LGPL-3",
    "development_status": "Production/Stable",
    "depends": ["purchase","mail"],
    "data": [
        # views
        'views/purchase_order.xml',
    ],
    "sequence": 1,
    'installable': True,
    'auto_install': False,
    'application': True,
}
