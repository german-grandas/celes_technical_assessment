import unittest
from datetime import datetime

from server.api import app
from server.models.sale import SaleDataModel, db
from server.controllers.sales_controller import SalesController


class TestSalesController(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.db = db
        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        with self.app.app_context():
            self.db.drop_all()

    def test_get_sales_by_employee(self):
        with self.app.app_context():
            sales_data = SaleDataModel(
                KeyEmployee=1,
                KeyProduct=101,
                KeyStore=201,
                KeyDate=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
                TicketId=1001,
                Amount=50.0,
                CostAmount=40.0,
                DiscAmount=5.0,
            )
            self.db.session.add(sales_data)
            self.db.session.commit()

            result = SalesController.get_sales_by_employee(
                employee=1, date_range=("2023-01-01", "2023-01-02")
            )
        expected_result = [
            {
                "KeyProduct": 101,
                "KeyStore": 201,
                "KeyDate": "2023-01-01",
                "Amount": 50.0,
                "CostAmount": 40.0,
                "DiscAmount": 5.0,
            }
        ]
        self.assertEqual(len(expected_result), len(result))
