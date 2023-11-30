{
  'name': 'Custom Contact Inherit',
    'summary': '""module to handle Data Confidential',
    'description': """Module to handle:
    - Name
    - No KTP
    - Work
    """,
    'sequence': 1,
    'author':'isbakhul lail',
    'website':'www.customcontact.com',
    'category':'Custom Contact Inherit',
    'depends':['contacts'],
    'data':[
      # security
      #'security/ir.model.access.csv',



      # views
      #'views/menu.xml',
      'views/res_partner_view.xml',




      # data

    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}