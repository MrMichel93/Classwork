"""Student self-checks for topic 03 worksheets."""

from starter_tests._support import WorksheetTestCase


class FunctionSelfChecks(WorksheetTestCase):
    def test_basic_functions(self):
        worksheet = self.load("03_functions", "01_basic_functions.py")
        self.assertEqual(self.require_callable(worksheet, "add_numbers")(5, 3), 8)
        self.assertTrue(self.require_callable(worksheet, "is_even")(8))
        self.assertEqual(self.require_callable(worksheet, "calculate_area")(10, 5), 50)

    def test_temperature_functions(self):
        worksheet = self.load("03_functions", "02_temperature_functions.py")
        self.assertEqual(self.require_callable(worksheet, "celsius_to_fahrenheit")(0), 32)
        self.assertAlmostEqual(self.require_callable(worksheet, "fahrenheit_to_celsius")(98.6), 37)
        self.assertEqual(self.require_callable(worksheet, "fahrenheit_to_kelvin")(32), 273.15)

    def test_string_functions(self):
        worksheet = self.load("03_functions", "03_string_functions.py")
        self.assertEqual(self.require_callable(worksheet, "make_uppercase")("hello"), "HELLO")
        self.assertEqual(self.require_callable(worksheet, "get_initials")("John", "Doe"), "J.D.")
        self.assertEqual(self.require_callable(worksheet, "count_vowels")("Python"), 1)

    def test_math_functions(self):
        worksheet = self.load("03_functions", "04_math_functions.py")
        self.assertEqual(self.require_callable(worksheet, "find_max")(15, 23), 23)
        self.assertEqual(self.require_callable(worksheet, "absolute_value")(-15), 15)
        self.assertEqual(self.require_callable(worksheet, "find_max_of_three")(15, 23, 19), 23)
