from run_app1 import app
import unittest

class FlaskBookshelfTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_root_route_type(self):
        result=self.app.get("/")
        #print(result)
        self.assertIsInstance(result.data,bytes)
        

    def test_root_route_status_code(self):
        result=self.app.get("/")
        #print(result)
        self.assertEqual(result.status_code,200)
    
    def test_root_route_body(self):
        result=self.app.get("/")
        #print(result)
        self.assertEqual(result.data,b"Welcome to our Library!")

