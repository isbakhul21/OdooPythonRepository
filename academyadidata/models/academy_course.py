from odoo import api, fields, models


class AcademyCourse(models.Model):

    _name = "academy.course"
    _inherit = ["mail.thread"]
    _description = "Course Info"

    name = fields.Char(string="Title",tracking=True)
    active = fields.Boolean(string="Active", default=True,tracking=True)

    description = fields.Text(string='Description',tracking=True)
    level = fields.Selection([
         ('beginner','Beginner'),
         ('intermediate','Intermediate'),
         ('advanced', 'Advanced'),
     ],string='Level',default='beginner',tracking=True)

    def action_confirm(self):
        print("hello world")


