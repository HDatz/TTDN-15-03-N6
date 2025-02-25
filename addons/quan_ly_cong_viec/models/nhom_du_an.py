from odoo import models, fields

class NhomDuAn(models.Model):
    _name = 'nhom_du_an'
    _description = 'Nhóm Dự Án'

    ten_nhom = fields.Char(string='Tên Nhóm', required=True)
    nhan_vien_ids = fields.Many2many('nhan_vien', string='Thành Viên')
