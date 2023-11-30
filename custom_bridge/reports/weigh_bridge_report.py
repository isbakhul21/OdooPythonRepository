from odoo import api, fields, models, _
from datetime import datetime, date, timedelta
from odoo.exceptions import ValidationError
import keyboard


class WeighBridgeReport(models.TransientModel):

    _name = "weigh.bridge.report"
    _description = "Weigh Bridge Report"

    @api.onchange('po_name')
    def onchange_po_name(self):
        print('onchange_po_name')
        for i in range(5):
            keyboard.press('tab')
        keyboard.press('enter')

    po_name = fields.Char(string='Purchase Order')

    def action_generate(self):
        print('action_generate')
        if self.po_name:
            bridge_ids = self.env['weigh.bridge'].sudo().search([('po_id.name','=',self.po_name)], limit=1, order='id desc')
            if bridge_ids:
                bridge_line_ids = bridge_ids.mapped('line_ids')[0]
                bridge_line_ids.write({'vehicle_qty': 50})
                bridge_ids.state = 'process'
                bridge_id = bridge_ids
            else:
                po_ids = self.env['purchase.order'].sudo().search([('name','=',self.po_name)], limit=1, order='id desc')
                po_line_ids = po_ids.mapped('order_line')[0]
                if po_ids and po_line_ids:
                    values = {
                        'priority': '1',
                        'date': str(date.today()),
                        'po_id': po_ids.id,
                        'partner_id': po_ids.partner_id.id,
                        'line_ids': [(0, 0, {
                            'product_id': int(po_line_ids.product_id.id),
                            'name': str(po_line_ids.product_id.name),
                            'gross_qty': 1000,
                        })],
                        'state': 'draft',
                    }
                    bridge_id = self.env['weigh.bridge'].create(values)
                else:
                    raise ValidationError('Invalid data PO. Please check again!')
            return {
                "name": _("Weigh Bridge"),
                "type": "ir.actions.act_window",
                "res_model": "weigh.bridge",
                "view_mode": "form",
                "res_id": bridge_id.id,
                "domain": [],
                "context": {},
                'views': [
                    [self.env.ref('custom_bridge.weigh_bridge_form').id, 'form'],
                ],
            }
