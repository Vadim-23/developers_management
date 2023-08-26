from odoo import fields, models


class AddDeveloperWizard(models.TransientModel):
    _name = 'add_developer.wizard'
    _description = 'Add Developer Wizard'

    developer_ids = fields.Many2many('developers_management.developer',
                                     string='Developers')
    company_id = fields.Many2one('developers_management.company',
                                 string='Company')

    def add_developer(self):
        # return the list of developers
        for developer in self.developer_ids:
            developer.company_id = self.company_id.id
