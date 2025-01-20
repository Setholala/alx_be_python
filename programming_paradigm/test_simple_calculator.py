import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(6, 0), 6)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6, 0), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 0), None)

        self.assertEqual(self.calc.divide(5, 1), 5)
        
