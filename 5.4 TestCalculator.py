import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(5, 6), 11)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(5, 6), 30)
    def test_subtruct(self):
        self.assertEqual(self.calculator.subtruct(15, 6), 9)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)
    def test_pov(self):
        self.assertEqual(self.calculator.pov(4, 2, 2), 36)
    def test_square(self):
        self.assertEqual(self.calculator.square(16, 4), 2)

if __name__ == '__main__':
    unittest.main()
