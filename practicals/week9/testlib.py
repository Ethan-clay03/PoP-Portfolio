import unittest
import types

class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(6, 0)

    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("hello", " world"), "hello world")

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
        with self.assertRaises(ValueError):
            find_max([])

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3]), 1)
        with self.assertRaises(ValueError):
            find_min([])

    def test_sort_list(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3]), [1, 2, 3])

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")

# ___ task 1

# Integers: 
def assert_equal(a,b):
    msg = ''
    if a != b:
        raise AssertionError(msg)

# pass the value 42 to the function
def test_value_1(x):
    assert_equal(x,42)
# pass the value 0 to the function
def test_value_2(x):
    assert_equal(x,0)
# pass the value 
# Two Billion One Hundred Forty-Seven Million 
# Four Hundred Eighty-Three Thousand
#  Six Hundred Forty-Seven:
def test_value_3(x):
    assert_equal(x, 2147483647)

# Floats: 

# pass the value 1.1
def test_value_4(x):
    assert_equal(x, 1.1)
# pass the function 0.001
def test_value_5(x):
    assert_equal(x, 0.001)
# pass the value of pi to 4 decimal places
def test_value_6(x):
    assert_equal(x, 3.1416)

# Strings: 

# pass the function the string hello
def test_value_7(x):
    assert_equal(x, 'hello')

# pass the function the string Hello
def test_value_8(x):
    assert_equal(x, 'Hello')

# pass the function the string 'hello world!'
def test_value_9(x):
    assert_equal(x, 'hello world!')

# Booleans:

# pass the boolean value true 
def test_value_10(x):
    assert_equal(x, True)
# pass the boolean value false 
def test_value_11(x):
    assert_equal(x, False)

# Lists: 

# pass a list containing numbers 1 - 5
def test_value_12(x):
    assert_equal(x, [1,2,3,4,5])

# pass a list containing three integers with the value of one
def test_value_13(x):
    assert_equal(x, [1,1,1])

# pass a list with the strings 'hello' 'world' '!'
# nb: there should be no spaces and the list should be 3 elements long...
def test_value_14(x):
    assert_equal(x, ['hello', 'world', '!'])

# Tuples:

# pass a tuple that contains the name 'ben' and the age 25
# this should be represented as a tuple with a string and integer value
def test_value_15(x):
    assert_equal(x,('ben', 25))

# pass a tuple that represents the origin on a graph using decimal values
def test_value_16(x):
    assert_equal(x, (0.0, 0.0))

# Dictionary: 

# Create a dictionary that contains the name 'ben' and the age 25
# this should be contain approriate keys and values of a string and integer respectively
def test_value_17(x):
    assert_equal(x, {"name": "ben", "age": 25})

def testTaskExample(x):
    None
def test_task2_1(x):
    assert_equal(x, 100/2)
def test_task2_2(x):
    assert_equal(x, 2.0 * 0.3)
def test_task2_3(x):
    assert_equal(x, 10 > 5)
def test_task2_4(x):
    assert_equal(x, 10 & 3)
def test_task2_5(x):
    assert_equal(x, True)
def test_task2_6(x):
    assert_equal(x, 1.5)
def test_task2_7(x):
    assert_equal(x, 10 / 5)
def test_task2_8(x):
    assert_equal(x, True or False)
def test_task2_9(x):
    assert_equal(x, 400)
def test_task2_10(x):
    assert_equal(x, 2)
def test_task2_11(x):
    assert_equal(x, 20*20)

from math import pi
def test_task2_12(x):
    assert_equal(x, pi * 2 ** 2)
def test_task2_13(x):
    assert_equal(x, (3 + 7 + 4) / 3 )
def test_task2_14(x):
    assert_equal(x, 2*299792458*299792458)
def test_task2_15(x):
    assert_equal(x, 64)
    
# Task 3
test_cases = TestFunctions()
def test_task3_add(x):
    assert_equal()


