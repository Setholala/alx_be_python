import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.a = 6
        self.b = 0
        self.calc = SimpleCalculator()

    def test_addition(self):
        result = self.calc.add(self.a, self.b)
        self.assertEqual(result, 6)

    def test_subtract(self):
        result = self.calc.subtract(self.a, self.b)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calc.multiply(self.a, self.b)
        self.assertEqual(result, 0)

    def test_divide(self):
        result = self.calc.divide(self.a, self.b)
        self.assertEqual(result, None)

        self.assertEqual(self.calc.divide(5, 1), 5)
        
