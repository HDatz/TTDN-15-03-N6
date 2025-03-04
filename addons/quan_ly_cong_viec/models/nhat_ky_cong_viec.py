from odoo import api, models, fields

from odoo.exceptions import ValidationError


class NhatKyCongViec(models.Model):
    _name = 'nhat_ky_cong_viec'
    _description = 'Nhật Ký Công Việc'

    cong_viec_id = fields.Many2one('cong_viec', string='Công Việc', ondelete='cascade')
    du_an_id = fields.Many2one('du_an', string='Dự Án', related='cong_viec_id.du_an_id', store=True)

    # Nhân viên thực hiện công việc
    nhan_vien_ids = fields.Many2many('nhan_vien', string='Người Thực Hiện', ondelete='cascade')

    ngay_thuc_hien = fields.Datetime(string='Ngày Thực Hiện', default=fields.Datetime.now)
    thoi_gian = fields.Float(string='Thời Gian (giờ)', digits=(6, 2))
    trang_thai = fields.Selection([
        ('chua_hoan_thanh', 'Chưa Hoàn Thành'),
        ('hoan_thanh', 'Hoàn Thành'),
        ('hoan_thanh_xuat_sac', 'Hoàn Thành Xuất Sắc'),
    ], string='Trạng Thái', default='chua_hoan_thanh')

    # danh_gia_nhan_vien_ids = fields.One2many('danh_gia_nhan_vien', 'nhat_ky_cong_viec_id', string='Đánh Giá Nhân Viên')

    
    @api.onchange('cong_viec_id')
    def _onchange_cong_viec(self):
        if self.cong_viec_id:
            self.nhan_vien_ids = [(6, 0, self.cong_viec_id.nhan_vien_ids.ids)]
        else:
            self.nhan_vien_ids = [(5, 0, 0)]  # Xóa danh sách nếu không có công việc nào được chọn


    @api.constrains('nhan_vien_ids')
    def _check_nhan_vien_ids(self):
        """Đảm bảo nhân viên thực hiện trong Nhật Ký Công Việc phải thuộc danh sách nhân viên tham gia Công Việc"""
        for record in self:
            if record.cong_viec_id:
                allowed_nhan_vien_ids = record.cong_viec_id.nhan_vien_ids.ids
                selected_nhan_vien_ids = record.nhan_vien_ids.ids
                
                # Kiểm tra xem có nhân viên nào không thuộc danh sách công việc không
                invalid_nhan_vien = set(selected_nhan_vien_ids) - set(allowed_nhan_vien_ids)
                if invalid_nhan_vien:
                    raise ValidationError("Người thực hiện phải thuộc danh sách nhân viên tham gia công việc.")