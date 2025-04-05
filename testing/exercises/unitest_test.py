import unittest

from .code import multiply, divide, reverse_string


class MultiplyTest(unittest.TestCase):
    def test_positives(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_negatives(self):
        self.assertEqual(multiply(-2, -5), 10)

    def test_positive_negative(self):
        self.assertEqual(multiply(2, -5), -10)


class ReverseStringTest(unittest.TestCase):
    def test_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

    def test_empty(self):
        self.assertEqual(reverse_string(''), '')


class DivideTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(28, 7), 4)

    def test_divide_zero(self):
        self.assertRaises(ValueError, divide, 7, 0)
