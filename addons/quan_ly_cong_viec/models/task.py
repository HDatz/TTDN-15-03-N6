from odoo import models, fields

class Task(models.Model):
    _name = 'project.task'
    _description = 'Project Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('project.management', string='Project')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    deadline = fields.Date(string='Deadline')
    stage_id = fields.Many2one('task.stage', string='Stage')
    work_log_ids = fields.One2many('work.log', 'task_id', string='Work Logs')
