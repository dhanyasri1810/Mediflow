
import unittest
from app import app, init_db, DB_PATH


class MediFlowTests(unittest.TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_missing_fields(self):
        response = self.client.post(
            "/appointments",
            json={"patient_name": "Sample Patient"}
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
