from odoo import models, fields, api

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ho_va_ten'

    ma_dinh_danh = fields.Char("Mã Định Danh", required=True, index=True)
    ngay_sinh = fields.Date("Ngày Sinh")  
    que_quan = fields.Char("Quê Quán")  
    email = fields.Char("Email") 
    so_dien_thoai = fields.Char("Số Điện Thoại")  
    lich_su_lam_viec_ids = fields.One2many('lich_su_lam_viec', 'nhan_vien_id', string="Lịch Sử Làm Việc")
    nhom_du_an_ids = fields.Many2many('nhom_du_an', string='Nhóm Dự Án')

    ho_va_ten = fields.Char("Họ và Tên", compute='_tinh_ho_va_ten', store=True)
    ho_ten_dem = fields.Char("Họ Tên Đệm")
    ten = fields.Char("Tên")

    @api.depends("ho_ten_dem", "ten")
    def _tinh_ho_va_ten(self):
        for record in self:
            record.ho_va_ten = f"{record.ho_ten_dem} {record.ten}".strip()

    @api.onchange("ten", "ho_ten_dem")
    def _onchange_tinh_ma_dinh_danh(self):
        for record in self:
            if record.ho_ten_dem and record.ten:
                record.ma_dinh_danh = f"{record.ho_ten_dem} {record.ten}".upper()
            else:
                record.ma_dinh_danh = False