from odoo import models, fields

class TaskStage(models.Model):
    _name = 'task.stage'
    _description = 'Task Stage'

    name = fields.Char(string='Stage Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
