"""Tests for function solutions."""

import unittest

from solution_loader import load_solution


class FunctionTests(unittest.TestCase):
    def test_basic_functions(self):
        functions = load_solution("03_functions", "01_basic_functions.py")
        self.assertEqual(functions.add_numbers(5, 3), 8)
        self.assertTrue(functions.is_even(8))
        self.assertEqual(functions.power(3), 9)

    def test_temperature_functions(self):
        functions = load_solution("03_functions", "02_temperature_functions.py")
        self.assertEqual(functions.fahrenheit_to_kelvin(32), 273.15)

    def test_string_functions(self):
        functions = load_solution("03_functions", "03_string_functions.py")
        self.assertEqual(functions.get_initials("John", "Doe"), "J.D.")
        self.assertEqual(functions.count_vowels("Python Programming"), 4)

    def test_math_functions(self):
        functions = load_solution("03_functions", "04_math_functions.py")
        self.assertEqual(functions.find_max_of_three(15, 23, 19), 23)
        self.assertAlmostEqual(functions.calculate_bmi(72, 1.8), 22.2222222222)
