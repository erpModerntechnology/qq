from odoo import api, fields, models
class ProjectTaskDAte(models.Model):
    _inherit = 'project.task'
    start_date = fields.Date(
        string='Start Date',
        required=False)
    end_date = fields.Date(
        string='End Date',
        required=False)


