{
    'name' : 'Report Manufacture',
    'summary': '""module to handle Report Manufacture',
    'description': """Module to handle:
    - Report Efisiensi
    - Report Tune Up
    - Report Schedule Machine
    """,
    'sequence': -99,
    'author':'isbakhul lail',
    'website':'www.ReportManufacture.com',
    'category':'reportmanufacture',
    'depends':['base','mrp','mail'],
    'data':[
      # security
      'security/ir.model.access.csv',
      #
      #
      #
      # views
      'views/menu.xml',
      'views/report_manufacture_view.xml',
      'views/mrp_production.xml',
      #
      #
      #
      #
      # data

    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}