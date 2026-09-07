"""Student self-checks for topic 05 worksheets."""

from starter_tests._support import WorksheetTestCase


class StringSelfChecks(WorksheetTestCase):
    def test_string_basics_output(self):
        worksheet = self.load("05_strings", "01_string_basics.py")
        self.assert_output_contains(
            worksheet, "H", "!", "Hello", "Python!", "John Doe",
            instruction="print indexing/slicing results and the concatenated full name.",
        )

    def test_string_methods_output(self):
        worksheet = self.load("05_strings", "02_string_methods.py")
        self.assert_output_contains(
            worksheet, "PYTHON PROGRAMMING", "Python Programming", "Hello World", "7",
            instruction="print the required transformations, stripped phrase, and programming index.",
        )

    def test_string_formatting_output(self):
        worksheet = self.load("05_strings", "03_string_formatting.py")
        self.assert_output_contains(
            worksheet, "My name is Alice and I am 25 years old", "Total cost: $59.97", "3.14", "1,234,567",
            instruction="use f-strings to print the person, price, rounded pi, and comma-formatted number.",
        )

    def test_string_iteration_output(self):
        worksheet = self.load("05_strings", "04_string_iteration.py")
        self.assert_output_contains(
            worksheet, "PPyytthhoonn",
            instruction="iterate through 'Python' and print the doubled-character result.",
        )
