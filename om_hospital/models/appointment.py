from odoo import  api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("TOMBOL DI KLIK cok ")

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    ref = fields.Char(string='Reference')
    gender = fields.Selection(tracking=True, related='patient_id.gender')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    prescription = fields.Html(string="Prescription")
    pharmamcy_line_ids = fields.One2many("appointment.pharmacy.line", "appointment_id", string="Pharmacy Lines")



class AppointmentPharmacyLine(models.Model):
    _name = "appointment.pharmacy.line"
    _description = "Appointment Pharmacy Line"

    product_id = fields.Many2one("product.product", required=True)
    price_unit = fields.Float(string="Price", related="product_id.list_price")
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")











