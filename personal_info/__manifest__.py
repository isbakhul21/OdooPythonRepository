{
  'name': 'Personal Info',
    'summary': '""module to handle Data Confidential',
    'description': """Module to handle:
    - Name
    - No KTP
    - Work
    """,
    'sequence': 1,
    'author':'isbakhul lail',
    'website':'www.PersonalInfo.com',
    'category':'personalinfo',
    'depends':['base','contacts'],
    'data':[
      # security
      'security/ir.model.access.csv',



      # views
      'views/menu.xml',
      'views/family_card_view.xml',




      # data

    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}