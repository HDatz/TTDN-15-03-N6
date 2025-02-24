from odoo import models, fields

class WorkLog(models.Model):
    _name = 'work.log'
    _description = 'Work Log'

    task_id = fields.Many2one('project.task', string='Task')
    user_id = fields.Many2one('res.users', string='User')
    work_date = fields.Datetime(string='Work Date', default=fields.Datetime.now)
    duration = fields.Float(string='Duration (hours)')
    description = fields.Text(string='Description')
