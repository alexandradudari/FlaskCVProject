import unittest
from app import app


class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_personal(self):
        response = self.app.get('/personal')
        self.assertEqual(response.status_code, 200)

    def test_experience(self):
        response = self.app.get('/experience')
        self.assertEqual(response.status_code, 200)

    def test_certifications(self):
        response = self.app.get('/certifications')
        self.assertEqual(response.status_code, 200)

    def test_education(self):
        response = self.app.get('/education')
        self.assertEqual(response.status_code, 200)
