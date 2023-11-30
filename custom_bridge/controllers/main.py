# from odoo.http import request, Response
# from odoo import http
# from datetime import datetime, date, timedelta
# import json
#
# headers_json = {'Content-Type': 'application/json'}
#
#
# class Controller(http.Controller):
#
#     @http.route('/weigh-bridge-quantity', auth='none', methods=['GET'], csrf=False)
#     def weigh_bridge_quantity(self, **kwargs):
#         print('weigh_bridge_quantity')
#         data = [{'quantity': 50}]
#         return Response(json.dumps(data), headers=headers_json)
#
#     @http.route('/weigh-bridge', auth='none', methods=['POST'], csrf=False)
#     def weigh_bridge(self, name, vehicle_driver, vehicle_number, quantity, **kwargs):
#         weigh_bridge_ids = request.env['weigh.bridge'].sudo().search([('name','=',str(name)),('vehicle_driver_id.name','=',str(vehicle_driver)),('vehicle_number','=',str(vehicle_number)),('state','=','draft')], limit=1, order='id desc')
#         if weigh_bridge_ids:
#             weigh_bridge_ids.mapped('line_ids')[0].vehicle_qty = float(quantity)
#             weigh_bridge_ids.state = 'process'
#         else:
#             partner_ids = request.env['res.partner'].sudo().search([('name','=','Cooperative')], limit=1, order='id desc')
#             vehicle_driver_ids = request.env['res.partner'].sudo().search([('name','=',str(vehicle_driver))], limit=1, order='id desc')
#             product_ids = request.env['product.template'].sudo().search([('name','=','[TBS] Tandan Buah Segar')], limit=1, order='id desc')
#             values = {
#                 'priority': '1',
#                 'name': str(name),
#                 'date': str(date.today()),
#                 'partner_id': partner_ids.id,
#                 'vehicle_driver_id': vehicle_driver_ids.id,
#                 'vehicle_number': str(vehicle_number),
#                 'line_ids': [(0, 0, {
#                     'product_id': int(product_ids.id),
#                     'name': str(product_ids.name),
#                     'gross_qty': float(quantity),
#                 })],
#             }
#             request.env['weigh.bridge'].create(values)
#         data = [{'status': 'Success'}]
#         return Response(json.dumps(data), headers=headers_json)
