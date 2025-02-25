from odoo import models, fields

class LichSuLamViec(models.Model):
    _name = 'lich_su_lam_viec'
    _description = 'Bảng chứa thông tin Lịch sử làm việc'
    _rec_name = 'ten_lich_su'

    ten_lich_su = fields.Char("Tên Lịch Sử", required=True)
    nhan_vien_id = fields.Many2one("nhan_vien", string="Nhân Viên", required=True, ondelete='cascade')
    cong_viec_id = fields.Many2one("cong_viec", string="Công Việc", ondelete='cascade')
