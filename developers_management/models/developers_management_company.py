from odoo import models, fields


class Company(models.Model):
    _name = 'developers_management.company'
    _description = 'Company Management'
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name must be unique'),
    ]

    name = fields.Char(required=True)
    address = fields.Text()
    developer_ids = fields.One2many('developers_management.developer',
                                    'company_id', string='Developers')

    def add_developer(self):
        # return the list of developers
        return {
            'name': 'Add Developer',
            'view_mode': 'form',
            'res_model': 'add_developer.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': {'default_company_id': self.id}
        }
