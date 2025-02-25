from odoo import models, fields

class NhatKyCongViec(models.Model):
    _name = 'nhat_ky_cong_viec'
    _description = 'Nhật Ký Công Việc'

    cong_viec_id = fields.Many2one('cong_viec', string='Công Việc', required=True, ondelete='cascade')
    du_an_id = fields.Many2one('du_an', string='Dự Án', related='cong_viec_id.du_an_id', store=True)
    nhan_vien_id = fields.Many2one('nhan_vien', string='Người Thực Hiện', required=True, ondelete='cascade')
    ngay_thuc_hien = fields.Datetime(string='Ngày Thực Hiện', default=fields.Datetime.now)
    thoi_gian = fields.Float(string='Thời Gian (giờ)', digits=(6, 2))
    mo_ta = fields.Text(string='Mô Tả')
