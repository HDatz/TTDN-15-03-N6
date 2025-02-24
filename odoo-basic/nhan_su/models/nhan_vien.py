from odoo import models, fields

class NhanVien(models.Model):
    _name = 'nhan.su.nhanvien'  # Tên model trong Odoo
    _description = 'Model Nhân Viên'

    # Các trường dữ liệu của nhân viên
    ma_dinh_danh = fields.Char(string="Mã định danh", required=True)
    ho_ten = fields.Char(string="Họ và Tên", required=True)
    ngay_sinh = fields.Date(string="Ngày Sinh")
    que_quan = fields.Char(string="Quê Quán")
    email = fields.Char(string="Email")
    so_dien_thoai = fields.Char(string="Số điện thoại")
