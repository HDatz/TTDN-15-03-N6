from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Công Việc Dự Án'
    _rec_name = 'ten_cong_viec'

    ten_cong_viec = fields.Char(string='Tên Công Việc', tracking=True)
    mo_ta = fields.Text(string='Mô Tả')
    du_an_id = fields.Many2one('du_an', string='Dự Án', required=True, ondelete='cascade')

    # Danh sách nhân viên tham gia công việc
    nhan_vien_ids = fields.Many2many('nhan_vien', 'cong_viec_nhan_vien_rel', 'cong_viec_id', 'nhan_vien_id', string='Nhân Viên Tham Gia')

    # Hạn chót công việc
    han_chot = fields.Datetime(string='Hạn Chót', tracking=True)

    # Giai đoạn công việc
    giai_doan_id = fields.Many2one('giai_doan_cong_viec', string='Giai Đoạn', tracking=True)

    nhat_ky_cong_viec_ids = fields.One2many('nhat_ky_cong_viec', 'cong_viec_id', string='Nhật Ký Công Việc')

    thoi_gian_con_lai = fields.Char(string="Thời Gian Còn Lại", compute="_compute_thoi_gian_con_lai", store=True)
    
    danh_gia_nhan_vien_ids = fields.One2many('danh_gia_nhan_vien', 'cong_viec_id', string='Đánh Giá Nhân Viên')

    @api.depends('han_chot')
    def _compute_thoi_gian_con_lai(self):
        """Tính toán thời gian còn lại trước hạn chót"""
        for record in self:
            if record.han_chot:
                now = datetime.now()
                delta = record.han_chot - now
                if delta.total_seconds() > 0:
                    days = delta.days
                    hours = delta.seconds // 3600
                    record.thoi_gian_con_lai = f"{days} ngày, {hours} giờ"
                else:
                    record.thoi_gian_con_lai = "Hết hạn"
            else:
                record.thoi_gian_con_lai = "Chưa có hạn chót"

    
    @api.onchange('du_an_id')
    def _onchange_du_an_id(self):
        """Khi chọn dự án, tự động lấy danh sách nhân viên từ dự án"""
        if self.du_an_id:
            self.nhan_vien_ids = [(6, 0, self.du_an_id.nhan_vien_ids.ids)]

            
    @api.constrains('du_an_id')
    def _check_du_an_tien_do(self):
        for record in self:
            if record.du_an_id and record.du_an_id.tien_do_du_an == 'hoan_thanh':
                raise ValidationError("Không thể thêm công việc vào dự án đã hoàn thành.")
            