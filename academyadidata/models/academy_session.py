from odoo import  api, fields, models


class AcademySession(models.Model):

    _name = 'academy.session'
    _description = 'Session Info'

    name = fields.Char(string='Title')

    session_number = fields.Char(string="Session Number",
                                 default=lambda self:self.env['ir.sequence'].next_by_code('session.sequence'))