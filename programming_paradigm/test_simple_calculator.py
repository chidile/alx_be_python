import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), 5)
        self.assertEqual(self.calc.subtract(-1, 1), 0)
        
    def test_multiplication(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.multiply(2, 3), 5)
        self.assertEqual(self.calc.multiply(-1, 1), 0)
        
    def test_division(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.divide(2, 3), 5)
        self.assertEqual(self.calc.divide(-1, 1), 0)
        

# Remember to write additional test methods for subtract, multiply, and divide.