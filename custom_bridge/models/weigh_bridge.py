from odoo import api, fields, models
from datetime import datetime, date, timedelta


class WeighBridge(models.Model):

    _name = "weigh.bridge"
    _inherit = "mail.thread"
    _description = "Weigh Bridge"
    _rec_name = "name"
    _order = "id desc"

    @api.onchange('state')
    def onchange_state(self):
        for this in self:
                this.sync_stock_picking_by_cron()

    priority = fields.Selection([
        ('0','Normal'),
        ('1','Urgent')
    ],string='Priority',default='0',index=True,tracking=True)
    name = fields.Char(string='No Documents',default=lambda self: self.env['ir.sequence'].next_by_code('weigh.bridge'),tracking=True)
    date = fields.Date(string='Date',tracking=True)
    po_id = fields.Many2one('purchase.order',string='Purchase Order',tracking=True)
    partner_id = fields.Many2one('res.partner',string='Vendor',tracking=True)
    vehicle_driver_id = fields.Many2one('res.partner',string='Vehicle Driver',tracking=True)
    vehicle_number = fields.Char(string='Vehicle Number',tracking=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('process','Process'),
        ('done','Done'),
        ('cancel','Cancel'),
    ],string='Status',default='draft',tracking=True)
    notes = fields.Text(string='Notes',tracking=True)
    line_ids = fields.One2many('weigh.bridge.line','weigh_bridge_id',relation='weigh_bridge_line_ids_rel',column1='weigh_bridge_id',column2='weigh_bridge_line_id',string='Weigh Bridge Line',tracking=True)

    def sync_stock_picking_by_cron(self):
        records = self.sudo().search([('date','>=',str(date.today() - timedelta(days=1))),('state','=','process')], order='id asc')
        print('records : ', records)
        for this in records:
            weigh_bridge_line_ids = this.mapped('line_ids')[0]
            print('weigh_bridge_line_ids')
            stock_move_ids = self.env['stock.move'].sudo().search([('picking_id.purchase_id','=',this.po_id.id),('state','!=','done')], limit=1, order='id desc')
            stock_move_ids.quantity_done = weigh_bridge_line_ids.net_qty
            this.state = 'done'


class WeighBridgeLine(models.Model):

    _name = "weigh.bridge.line"
    _inherit = "mail.thread"
    _description = "Weigh Bridge Line"
    _rec_name = "name"
    _order = "id desc"

    @api.onchange('product_id')
    def onchange_product_id(self):
        for this in self:
            name = this.product_id.name
            this.name = name

    @api.depends('gross_qty','vehicle_qty')
    def _getNetQty(self):
        for this in self:
            net_qty = this.gross_qty - this.vehicle_qty if this.gross_qty else 0
            this.net_qty = net_qty

    weigh_bridge_id = fields.Many2one('weigh.bridge',string='Weigh Bridge',tracking=True)
    product_id = fields.Many2one('product.template',string='Products',tracking=True)
    name = fields.Char(string='Description',tracking=True)
    date = fields.Date(string='Date',related='weigh_bridge_id.date',store=True,tracking=True)
    gross_qty = fields.Float(string='Gross Qty',help='Gross Qty = Vehicle Qty + Net Qty',tracking=True)
    vehicle_qty = fields.Float(string='Vehicle Qty',tracking=True)
    net_qty = fields.Float(string='Net Qty',compute=_getNetQty,store=True,tracking=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('process','Process'),
        ('done','Done'),
        ('cancel','Cancel'),
    ],string='Status',related='weigh_bridge_id.state',store=True,tracking=True)