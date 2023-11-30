{
  'name': 'Odoo Academy adidata',
    'summary': '""module to handle Course and Sessions',
    'description': """Module to handle:
    - Course
    - Sessions
    -Attendees
    """,
    'license':'OPL-1',
    'author':'isbakhul',
    'website':'www.odoo.com',
    'category':'Custom Modules/Tech Training',
    'depends':['base','mail'],
    'data':[
      # security
      'security/ir.model.access.csv',

      # views
      'views/academy_course.xml',
      'demo/course_demo.xml',
      # 'views/academy_session.xml'

      # data
      'data/res_groups.xml',
      'data/ir_ui_menu.xml',
      'data/ir_sequence.xml',
    ],
    'demo': [
      # 'demo/course_demo.xml',
    ],
    'application': True,
    'installable': True,
}