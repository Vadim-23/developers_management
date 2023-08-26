from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestCompanyManagement(TransactionCase):

    def setUp(self):
        super(TestCompanyManagement, self).setUp()
        self.Company = self.env['developers_management.company']
        self.Developer = self.env['developers_management.developer']

    def test_create_company(self):
        # Створюємо компанію
        company_data = {
            'name': 'Acme Inc.',
            'address': '123 Main St',
        }
        company = self.Company.create(company_data)

        # Перевіряємо, чи створена компанія правильно
        self.assertEqual(company.name, 'Acme Inc.')
        self.assertEqual(company.address, '123 Main St')

    def test_unique_name_constraint(self):
        company_data_1 = {
            'name': 'ABC Corp.',
        }
        company_data_2 = {
            'name': 'ABC Corp.',
        }

        with self.assertRaises(ValidationError):
            self.Company.create(company_data_1)
            self.Company.create(company_data_2)

    def test_add_developer_action(self):
        company_data = {
            'name': 'XYZ Ltd.',
        }
        company = self.Company.create(company_data)

        action = company.add_developer()

        self.assertEqual(action['name'], 'Add Developer')
        self.assertEqual(action['view_mode'], 'form')
        self.assertEqual(action['res_model'], 'add_developer.wizard')
        self.assertEqual(action['type'], 'ir.actions.act_window')
        self.assertEqual(action['target'], 'new')
        self.assertEqual(action['context'], {'default_company_id': company.id})
