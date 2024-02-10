import unittest
from utils import welcome_message

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_welcome_message(self):
        self.assertEqual(welcome_message(), "<p>Hello, World!</p>")
    
if __name__ == '__main__':
    unittest.main()