from AirportSearch import app
import unittest

class MyTest(unittest.TestCase):
	# Ensure that flask is set up properly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/countries',content_type='html/text')
		self.assertEqual(response.status_code,200)

	# Ensure that search page loads correctly
	def test_home_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/countries',content_type='html/text')
		self.assertTrue(b'Search Airports' in response.data)

	# Ensure that dropdown exists
	def test_dropdown_exists(self):
		tester = app.test_client(self)
		response = tester.get('/countries',content_type='html/text')
		self.assertTrue(b'country' in response.data)

	# Ensure that autocomplete text field exists
	def test_textfield_exists(self):
		tester = app.test_client(self)
		response = tester.get('/countries',content_type='html/text')
		self.assertTrue(b'airportAutocomplete' in response.data)

	# Ensure that dropdown contains values or its empty
	def test_dropdown_value_exists(self):
		tester = app.test_client(self)
		response = tester.get('/countries',content_type='html/text')
		self.assertTrue(b'India' in response.data)

	# Ensure that after dropdown select whether we get the response or not
	def test_fetch_aiports(self):
		tester = app.test_client(self)
		response = tester.get('/get_airport_names?param=India',content_type='html/text')
		self.assertEqual(response.status_code,200)

	# Ensure that after dropdown select whether we get empty response or with values
	def test_fetch_aiports_values(self):
		tester = app.test_client(self)
		response = tester.get('/get_airport_names?param=India',content_type='html/text')
		self.assertTrue(b'Salem' in response.data)

if __name__ == '__main__' :
	unittest.main()
