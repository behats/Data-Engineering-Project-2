import unittest
import os
import requests

class FlaskTests(unittest.TestCase):
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		pass
	def tearDown(self):
		pass

	#test if the site respond 
	def test_a_interface(self):
		response = requests.get('http://localhost:5000')
		self.assertEqual(response.status_code,200)


if __name__=='__main__':
	unittest.main()
