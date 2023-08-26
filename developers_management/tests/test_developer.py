from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestDeveloperManagement(TransactionCase):

    def setUp(self):
        super(TestDeveloperManagement, self).setUp()
        self.Developer = self.env['developers_management.developer']

    def test_create_developer(self):
        # Створюємо розробника
        developer_data = {
            'name': 'John Doe',
            'type': 'front-end',
            'phone': '1234567890',
            'email': 'john@example.com',
        }
        developer = self.Developer.create(developer_data)

        # Перевіряємо, чи створений розробник правильно
        self.assertEqual(developer.name, 'John Doe')
        self.assertEqual(developer.type, 'front-end')
        self.assertEqual(developer.phone, '1234567890')
        self.assertEqual(developer.email, 'john@example.com')

    def test_unique_name_constraint(self):
        developer_data_1 = {
            'name': 'Alice',
            'type': 'front-end',
        }
        developer_data_2 = {
            'name': 'Alice',
            'type': 'backend',
        }

        with self.assertRaises(ValidationError):
            self.Developer.create(developer_data_1)
            self.Developer.create(developer_data_2)

    def test_compute_global_identification(self):
        developer_data = {
            'name': 'Alice',
            'type': 'front-end',
        }
        developer = self.Developer.create(developer_data)

        self.assertEqual(developer.global_identification, 'Alice-front-end')

        developer.write({'type': 'backend'})

        self.assertEqual(developer.global_identification, 'Alice-backend')
