from odoo import  api, fields, models

class MrpProduction(models.Model):
    _inherit = "mrp.production"
    _description = "mrp production"

    file_path_kernel = "C:/project/odoo16-addons/addons-dev/data_kernel/data_kernel.txt"
    with open(file_path_kernel, 'r') as file:
        data_kernel_raw = [line.strip() for line in file]
        data_kernel = data_kernel_raw[-1]

    file_path_shell = "C:/project/odoo16-addons/addons-dev/data_shell/data_shell.txt"
    with open(file_path_shell, 'r') as file:
        data_shell_raw = [line.strip() for line in file]
        data_shell = data_shell_raw[-1]
    #
    file_path_tandan_buah_segar = "C:/project/odoo16-addons/addons-dev/data_tandan_buah_segar/tandan_buah_segar.txt"
    with open(file_path_tandan_buah_segar, 'r') as file:
        data_tbs_raw = [line.strip() for line in file]
        data_tbs = data_tbs_raw[-1]

    file_path_air = "C:/project/odoo16-addons/addons-dev/data_air/data_air"
    with open(file_path_air, 'r') as file:
        data_air_raw = [line.strip() for line in file]
        data_air = data_air_raw[-1]

    file_path_crude_palm_oil = "C:/project/odoo16-addons/addons-dev/data_crude_palm_oil/data_crude_palm_oil.txt"
    with open(file_path_crude_palm_oil, 'r') as file:
        data_crude_palm_oil_raw = [line.strip() for line in file]
        data_crude_palm_oil = data_crude_palm_oil_raw[-1]


    def generate_mo_report(self):
        # print(self.id)
        # print(self.data_kernel)
        # print(type(self.data_kernel))
        # print(self.state)
        hasil = {
            'mrp_production_id': self.id,
            'status': self.state,
            'operation_time': self.date_planned_start,
            'shift': 1,
            'cpo': 0,
            'tanggal': self.date_planned_start,
             'kernel': 0,
             'shell': 0,
            'tbs': 0,
            'air': 0
        }

        check_report_mo = self.env['report.manufacture'].search([('mrp_production_id','=',self.id)], order='id desc')
        if not check_report_mo:
            self.env['report.manufacture'].create(hasil)
        else:
            check_report_mo.write(hasil)



    def action_update_mo(self):

        if self.product_id.name == 'Crude Palm Oil (CPO)':
            self.qty_producing = self.data_crude_palm_oil
            print("self.product_qty : ", self.product_qty)
        for move_id in self.move_raw_ids:
            if move_id.product_id.name == 'Tandan Buah Segar (TBS)':
                move_id.quantity_done = self.data_tbs
            if move_id.product_id.name == 'Air':
                move_id.quantity_done = self.data_air
        for move_id in self.workorder_ids:
            if move_id.name == 'STASIUN PEREBUSAN':
                move_id.duration = 8
            if move_id.name == 'STASIUN PEMERASAN':
                move_id.duration = 8
            if move_id.name == 'STATSIUN PENYARINGAN':
                move_id.duration = 8
        for move_id in self.move_byproduct_ids:
            if move_id.product_id.name == 'SHELL':
                move_id.quantity_done = self.data_shell
            if move_id.product_id.name == 'Kernel':
                move_id.quantity_done = self.data_kernel





    def generate_mo_report_all(self):
        hasil = {
            'mrp_production_id': self.id,
            'status': self.state,
            'operation_time': self.date_planned_start,
            'tanggal': self.date_planned_start,
            'kernel': self.data_kernel,
            'shell': self.data_shell,
             'tbs' : self.data_tbs,
            'air': self.data_air,
            'cpo': self.data_crude_palm_oil
        }

        check_report_mo = self.env['report.manufacture'].search([('mrp_production_id', '=', self.id)],
                                                                order='id desc')
        if not check_report_mo:
            self.env['report.manufacture'].create(hasil)
        else:
            check_report_mo.write(hasil)

















