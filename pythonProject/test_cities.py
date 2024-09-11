import unittest
from city import city_country
class Test_city_country(unittest.TestCase):

	def test_city_country(self):
		formatedname=city_country('Dhaka','Bangladesh')
		self.assertEqual(formatedname,'Dhaka, Bangladesh')

if __name__ == '__main__':
	unittest.main()