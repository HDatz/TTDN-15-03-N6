from odoo import api, models, fields

class NhatKyCongViec(models.Model):
    _name = 'nhat_ky_cong_viec'
    _description = 'Nhật Ký Công Việc'

    cong_viec_id = fields.Many2one('cong_viec', string='Công Việc', ondelete='cascade')
    du_an_id = fields.Many2one('du_an', string='Dự Án', related='cong_viec_id.du_an_id', store=True)
    nhan_vien_id = fields.Many2one('nhan_vien', string='Người Thực Hiện', ondelete='cascade')
    ngay_thuc_hien = fields.Datetime(string='Ngày Thực Hiện', default=fields.Datetime.now)
    thoi_gian = fields.Float(string='Thời Gian (giờ)', digits=(6, 2))
    mo_ta = fields.Text(string='Mô Tả')
    
    ten_du_an = fields.Char(related="du_an_id.ten_du_an",string='Tên Dự Án')
    # ho_va_ten =fields.Char(related="nhan_vien_id.ho_va_ten", string='Người Thực Hiện')
    
    @api.onchange('cong_viec_id')
    def _onchange_cong_viec(self):
        # Khi chọn công việc, tự động điền nhân viên thực hiện.
        if self.cong_viec_id:
            self.nhan_vien_id = self.cong_viec_id.nhan_vien_id