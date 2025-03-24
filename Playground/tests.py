import unittest
from .main import litres


class NoSpaceTests(unittest.TestCase):
    def test1(self):
        output = litres(3)
        self.assertEqual(output, 1)

    def test2(self):
        output = litres(6.7)
        self.assertEqual(output, 3)

    def test3(self):
        output = litres(11.8)
        self.assertEqual(output, 5)
