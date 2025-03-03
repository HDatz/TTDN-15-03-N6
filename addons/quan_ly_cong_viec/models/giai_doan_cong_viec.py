from odoo import models, fields

class GiaiDoanCongViec(models.Model):
    _name = 'giai_doan_cong_viec'
    _description = 'Giai Đoạn Công Việc'
    _rec_name = 'ten_giai_doan'

    ten_giai_doan = fields.Char(string='Tên Giai Đoạn', required=True)
    thu_tu = fields.Integer(string='Thứ Tự')
