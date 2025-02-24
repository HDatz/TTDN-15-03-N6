from odoo import models, fields

class PhongBan(models.Model):
    _name = "phong.ban"
    _description = "Quản lý Phòng Ban"
 
    ma_phong_ban = fields.Char("Mã Phòng Ban", required= True)
    ten_phong_ban = fields.Char("Tên Phòng Ban", required=True)

