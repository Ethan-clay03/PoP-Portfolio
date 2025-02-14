import unittest
from task2 import *

class TestTask2(unittest.TestCase):
    def test_example(self):
        # Test cases
        self.assertEqual(example('beep'), 'boop')
        self.assertEqual(example('meep'), 'nope')
    
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')
        self.assertEqual(fizz_buzz(5), 'Buzz')
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')
        self.assertEqual(fizz_buzz(7), '7')


if __name__ == '__main__':
    unittest.main()