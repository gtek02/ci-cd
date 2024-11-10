# tests/test_calculator.py

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    # Testy podstawowe
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)

    # Nowe testy
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)  # Sprawdzenie dodawania liczb ujemnych

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)  # Sprawdzenie odejmowania liczb ujemnych

    def test_multiply_with_negative(self):
        self.assertEqual(multiply(-2, 3), -6)  # Sprawdzenie mnożenia z liczbą ujemną

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1000000, 2000000), 2000000000000)  # Test z dużymi liczbami

    def test_divide_with_float(self):
        self.assertAlmostEqual(divide(5, 2), 2.5)  # Test dzielenia z wynikiem zmiennoprzecinkowym

if __name__ == '__main__':
    unittest.main()
