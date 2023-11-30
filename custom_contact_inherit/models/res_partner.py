from odoo import  api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "res partner"

    nomor_ktp = fields.Char(string="Nomor KTP", store=True, tracking=True)





