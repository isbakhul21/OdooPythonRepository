{
    "name": "[Custom] Bridge",
    "summary": "Responsive web client, community-supported",
    "description": "This module contains all the common features of Purchase.",
    "version": "1.0.0",
    "category": "Purchase",
    "author": "ISBAKHUL LAIL",
    "license": "LGPL-3",
    "development_status": "Production/Stable",
    "maintainers": ["ISBAKHUL LAIL"],
    "depends": ["purchase","mail"],
    "data": [
        # Security
        'security/ir.model.access.csv',

        # views
        "views/weigh_bridge.xml",
        "reports/views/weigh_bridge_report.xml",

        # data
        'data/ir_ui_menu.xml',
        'data/ir_cron.xml',
        'data/ir_sequence.xml',
    ],
    "sequence": 1,
    'installable': True,
    'auto_install': False,
    'application': True,
}
