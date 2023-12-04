import unittest
from datetime import datetime


from flask_sqlalchemy import SQLAlchemy

from server.api import app
from server.models.sale import SaleDataModel, db


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.app = app
        self.db = db
        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        with self.app.app_context():
            self.db.drop_all()

    def test_get_sales_by_employee_endpoint(self):
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

        headers = {"Authorization": "Bearer VALID_TOKEN"}
        response = self.client.get(
            "/getSalesByEmployee?employee_id=1&start_date=2023-01-01&end_date=2023-01-02",
            headers=headers,
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
        client_response = response.get_json().get("response")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(client_response), len(expected_result))
