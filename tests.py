import unittest
from flasktest import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
	app.config['SERVER_NAME'] = 'sub.flasktest.com'
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
	rv = self.app.get('/')
	print rv.data

if __name__ == '__main__':
    unittest.main()
