from odoo import models, fields, api

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Công Việc Dự Án'

    ten_cong_viec = fields.Char(string='Tên Công Việc', required=True, tracking=True)
    mo_ta = fields.Text(string='Mô Tả')
    du_an_id = fields.Many2one('du_an', string='Dự Án', required=True, ondelete='cascade')
    nhan_vien_id = fields.Many2one('nhan_vien', string='Người Phụ Trách', tracking=True)
    han_chot = fields.Date(string='Hạn Chót', tracking=True)
    giai_doan_id = fields.Many2one('giai_doan_cong_viec', string='Giai Đoạn', tracking=True)
    nhat_ky_cong_viec_ids = fields.One2many('nhat_ky_cong_viec', 'cong_viec_id', string='Nhật Ký Công Việc')
