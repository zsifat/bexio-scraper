import unittest
from func import Fullname

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """Test the Fullname function with example input."""
        name = Fullname('jane', 'smith')
        self.assertEqual(name, 'Jane Smith')

if __name__ == '__main__':
    unittest.main()
