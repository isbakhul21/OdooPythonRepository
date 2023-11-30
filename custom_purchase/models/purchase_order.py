from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from io import BytesIO
import base64
import qrcode


class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    @api.depends('name')
    def _getQrCode(self):
        for this in self:
            if qrcode and base64:
                qr = qrcode.QRCode(version=1,box_size=5,border=4,error_correction=qrcode.constants.ERROR_CORRECT_L)
                qr.add_data("No Documents PO : {}".format(str(this.name)))
                qr.make(fit=True)
                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                this.update({'qrcode': qr_image})
            else:
                raise ValidationError('Necessary Requirements To Run This Operation Is Not Satisfied')

    qrcode = fields.Binary('QRcode',compute=_getQrCode,store=True,tracking=True)

