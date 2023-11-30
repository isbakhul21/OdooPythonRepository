from odoo import  api, fields, models


class PersonalInfo(models.Model):

    _name = "personal.info"
    _description = "personal info"
    _rec_name = "partner_id"

    @api.depends('partner_id')
    def _getnomor_ktp(self):
        for this in self:
            nomor_ktp = str(this.partner_id.nomor_ktp)
            self.nomor_ktp = nomor_ktp

    partner_id = fields.Many2one('res.partner',  string="Name")
    nomor_ktp = fields.Char(string="Nomor KTP", compute=_getnomor_ktp, store=True, tracking=True)
    family_line_ids = fields.One2many('personal.family.line','personal_id', string="familyline_id" )


class PersonalFamilyLine(models.Model):

    _name = "personal.family.line"
    _description = "personal family line"

    personal_id = fields.Many2one('personal.info',string="personal ID",tracking=True)
    nama_anggota = fields.Char(string="Nama Anggota",tracking=True)
    status = fields.Selection([
        ('suami','Suami'),
        ('istri','Istri'),
        ('anak','Anak')], string="Status Hubungan")
    anak_ke = fields.Selection([
        ('1','Ke-1'),
        ('2','Ke-2'),
        ('3','Ke-3'),
    ],string='Description',default='',tracking=True)

    # @api.model
    # def create_anggota(self,values):
    #
    #     suami_exist = self.search_count([('status','=','suami')])
    #
    #     if not suami_exist:
    #         values['nama_anggota'] = 'Nama Suami'
    #         values['status'] = 'suami'
    #
    #     else:
    #         values['nama_anggota'] = "Nama Istri"
    #         values['status'] = "istri"
    #
    #     return super(PersonalFamilyLine, self).create_anggota(values)










