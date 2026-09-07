"""Tests for variables, expressions, and statements solutions."""

import unittest

from solution_loader import load_solution


class VariablesExpressionsStatementsTests(unittest.TestCase):
    def test_calculator(self):
        calculator = load_solution("01_variables_expressions_statements", "01_calculator.py")
        self.assertEqual(calculator.calculate(10, 5)["power"], 100000)

    def test_temperature_converter(self):
        converter = load_solution("01_variables_expressions_statements", "02_temperature_converter.py")
        self.assertEqual(converter.celsius_to_fahrenheit(0), 32)

    def test_shopping_cart(self):
        cart = load_solution("01_variables_expressions_statements", "03_shopping_cart.py")
        result = cart.calculate_cart([15.99, 23.50, 8.75], starting_money=60)
        self.assertAlmostEqual(result["total_cost"], 52.0992)
        self.assertAlmostEqual(result["money_left"], 7.9008)

    def test_area_calculator(self):
        calculator = load_solution("01_variables_expressions_statements", "04_area_calculator.py")
        self.assertEqual(calculator.rectangle_measurements(10, 5), (50, 30))
        self.assertAlmostEqual(calculator.triangle_area_for(8, 6), 24)
