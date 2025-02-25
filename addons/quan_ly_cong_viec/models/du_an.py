from odoo import models, fields

class DuAn(models.Model):
    _name = 'du_an'
    _description = 'Dự Án'

    ten_du_an = fields.Char(string='Tên Dự Án', required=True)
    mo_ta = fields.Text(string='Mô Tả')
    cong_viec_ids = fields.One2many('cong_viec', 'du_an_id', string='Công Việc')
    nhat_ky_cong_viec_ids = fields.One2many('nhat_ky_cong_viec', 'du_an_id', string='Nhật Ký Công Việc')
