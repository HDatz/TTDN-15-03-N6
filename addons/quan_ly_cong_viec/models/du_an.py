from odoo import models, fields, api
from datetime import datetime

class DuAn(models.Model):
    _name = 'du_an'
    _description = 'Dự Án'
    _rec_name = 'ten_du_an'

    ten_du_an = fields.Char(string='Tên Dự Án', required=True)
    mo_ta = fields.Text(string='Mô Tả')
    
    # Người phụ trách dự án
    nguoi_phu_trach_id = fields.Many2one('nhan_vien', string='Người Phụ Trách', ondelete='set null')

    # Danh sách nhân viên tham gia dự án
    nhan_vien_ids = fields.Many2many('nhan_vien', 'du_an_nhan_vien_rel', 'du_an_id', 'nhan_vien_id', string='Nhân Viên Tham Gia')

    # Danh sách tài nguyên
    tai_nguyen_ids = fields.One2many('tai_nguyen', 'du_an_id', string='Danh Sách Tài Nguyên')

    # Danh sách công việc thuộc dự án
    cong_viec_ids = fields.One2many('cong_viec', 'du_an_id', string='Công Việc')
    
    danh_gia_nhan_vien_ids = fields.One2many('danh_gia_nhan_vien', 'du_an_id', string='Đánh Giá Nhân Viên')
    # Tiến độ dự án
    tien_do_du_an = fields.Selection([
        ('chua_bat_dau', 'Chưa Bắt Đầu'),
        ('dang_thuc_hien', 'Đang Thực Hiện'),
        ('hoan_thanh', 'Hoàn Thành'),
        ('tam_dung', 'Tạm Dừng')
    ], string="Trạng Thái Dự Án", default='chua_bat_dau')

    nhat_ky_cong_viec_ids = fields.One2many('nhat_ky_cong_viec', 'du_an_id', string='Nhật Ký Công Việc')

    @api.model
    def create(self, vals):
        """ Đảm bảo người phụ trách có trong danh sách nhân viên tham gia khi tạo dự án """
        nguoi_phu_trach_id = vals.get('nguoi_phu_trach_id')
        nhan_vien_ids = vals.get('nhan_vien_ids', [(6, 0, [])])  # Mặc định là danh sách rỗng nếu không có

        if nguoi_phu_trach_id:
            # Lấy danh sách nhân viên hiện có
            nhan_vien_list = set(nhan_vien_ids[0][2]) if nhan_vien_ids else set()
            # Thêm người phụ trách vào danh sách
            nhan_vien_list.add(nguoi_phu_trach_id)
            vals['nhan_vien_ids'] = [(6, 0, list(nhan_vien_list))]

        return super(DuAn, self).create(vals)

    def write(self, vals):
        """ Đảm bảo người phụ trách có trong danh sách nhân viên tham gia khi cập nhật dự án """
        for record in self:
            nguoi_phu_trach_id = vals.get('nguoi_phu_trach_id', record.nguoi_phu_trach_id.id)
            nhan_vien_ids = vals.get('nhan_vien_ids', [(6, 0, record.nhan_vien_ids.ids)])

            if nguoi_phu_trach_id:
                nhan_vien_list = set(nhan_vien_ids[0][2]) if nhan_vien_ids else set()
                nhan_vien_list.add(nguoi_phu_trach_id)
                vals['nhan_vien_ids'] = [(6, 0, list(nhan_vien_list))]

        return super(DuAn, self).write(vals)