from odoo import  api, fields, models



class ReportManufacture(models.Model):

    _name = "report.manufacture"
    _description = "report manufacture"



    mrp_production_id = fields.Many2one('mrp.production', string="manufacture order")
    tanggal = fields.Date(string="Scheduled Date")
    shift = fields.Integer(string="Shift")
    tbs = fields.Float(string="Tandan Buah Segar")
    cpo = fields.Float(string="Crude Palm Oil")
    kernel = fields.Float(string="Kernel")
    shell = fields.Float(string="Shell")
    air = fields.Float(string="Air")
    operation_time = fields.Datetime(string="Operation Time")
    status = fields.Char(string="Status")

    file_path_tandan_buah_segar = "C:/project/odoo16-addons/addons-dev/data_tandan_buah_segar/tandan_buah_segar.txt"
    with open(file_path_tandan_buah_segar, 'r') as file:
        data_tbs_raw = [line.strip() for line in file]
        data_tbs = data_tbs_raw[-1]

    file_path_air = "C:/project/odoo16-addons/addons-dev/data_air/data_air"
    with open(file_path_air, 'r') as file:
        data_air_raw = [line.strip() for line in file]
        data_air = data_air_raw[-1]


    def action_test(self):

        print(self.mrp_production_id, type(self.mrp_production_id))

        self.mrp_production_id.action_confirm()
        print("CONFIRM MO")
        self.mrp_production_id.generate_mo_report_all()
        print("Generate MO")
        for workorder_id in self.mrp_production_id.workorder_ids:
            workorder_id.button_start()
            workorder_id.button_finish()

        self.mrp_production_id.button_mark_done()
        print("Mark As DOne")
        #untuk mengupdate MO yang sudah done
        self.mrp_production_id.action_update_mo()
        self.mrp_production_id.generate_mo_report_all()



















