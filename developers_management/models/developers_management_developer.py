from odoo import models, fields, api


class Developer(models.Model):
    _name = 'developers_management.developer'
    _description = 'Developer Management'
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name must be unique'),
    ]

    name = fields.Char(required=True)
    type = fields.Selection([
        ('front-end', 'Front-end'),
        ('backend', 'Back-end'),
        ('fullstack', 'Fullstack'),
        ('out-stuff', 'Out Stuff')
    ], required=True)
    global_identification = fields.Char(
        compute='_compute_global_identification')
    phone = fields.Char()
    email = fields.Char()
    address = fields.Text()
    birthdate = fields.Date()
    position = fields.Char()
    image_1920 = fields.Image(string='Image', max_width=1920, max_height=1920)
    company_id = fields.Many2one('developers_management.company')

    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for developer in self:
            developer.global_identification = \
                f'{developer.name}-{developer.type}'
