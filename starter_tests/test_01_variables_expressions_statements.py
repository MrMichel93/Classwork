"""Student self-checks for topic 01 worksheets."""

from starter_tests._support import WorksheetTestCase


class VariablesExpressionsStatementsSelfChecks(WorksheetTestCase):
    def test_calculator_output(self):
        worksheet = self.load("01_variables_expressions_statements", "01_calculator.py")
        self.assert_output_contains(
            worksheet, "15", "50", "2.0", "100000",
            instruction="print the calculator's sum, product, quotient, and power results.",
        )

    def test_temperature_converter_output(self):
        worksheet = self.load("01_variables_expressions_statements", "02_temperature_converter.py")
        self.assert_output_contains(
            worksheet, "25.0", "77.0", "298.15", "98.6",
            instruction="print the Celsius, Fahrenheit, Kelvin, and body-temperature conversions.",
        )

    def test_shopping_cart_output(self):
        worksheet = self.load("01_variables_expressions_statements", "03_shopping_cart.py")
        self.assert_output_contains(
            worksheet, "48.24", "52.0992", "7.9008",
            instruction="print the subtotal, tax-inclusive total, and money left from $60.",
        )

    def test_area_calculator_output(self):
        worksheet = self.load("01_variables_expressions_statements", "04_area_calculator.py")
        self.assert_output_contains(
            worksheet, "65.1", "33.4", "78.53975", "24",
            instruction="print rectangle area/perimeter, circle area, and triangle area.",
        )
