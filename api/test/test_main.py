import unittest
from urllib import response
from .. import create_app
from ..config import config_dist


class TestApi(unittest.TestCase):
    n = 12
    x1 = 3
    x2 = 4
    ackermann_excepted_output = "125"
    factorial_expected_output = "24"
    feibonacci_expected_output = "144"

    def setUp(self):
        self.app = create_app(config=config_dist['test'])
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.appctx.pop()
        self.app =None
        self.client = None


    def test_fibonacci(self):
        response = self.client.get(f'/Math/feibonacci/{self.n}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('UTF-8').strip('\n'), self.feibonacci_expected_output)

    def test_ackermann(self):
        response = self.client.get(f'/Math/ackermann/{self.x1}/{self.x2}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('UTF-8').strip('\n'), self.ackermann_excepted_output)

    def test_factorial(self):
        response = self.client.get(f'/Math/factorial/{self.x2}')
        assert response.status_code == 200
        self.assertEqual(response.data.decode('UTF-8').strip('\n'), self.factorial_expected_output)
