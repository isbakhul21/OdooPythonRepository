# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
   _inherit = 'sale.order'

   confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
   
   def action_confirm(self):
      #dibawah ini untuk memanggil fucntion original
      super(SaleOrder, self).action_confirm()
      #dibawah ini untuk memanggil function dari inherit
      print("ini teks dari funciton inherit.....................................")
      self.confirmed_user_id = self.env.user.id

