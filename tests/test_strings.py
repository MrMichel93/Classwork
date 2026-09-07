"""Tests for string solutions."""

import unittest

from solution_loader import load_solution


class StringTests(unittest.TestCase):
    def test_string_basics(self):
        basics = load_solution("05_strings", "01_string_basics.py")
        self.assertEqual(basics.describe_message("Hello, Python!")["last_seven"], "Python!")
        self.assertEqual(basics.middle_two_characters("Python"), "th")

    def test_string_methods(self):
        methods = load_solution("05_strings", "02_string_methods.py")
        self.assertEqual(methods.string_method_results()["programming_position"], 7)
        self.assertEqual(methods.case_transformations()[2], "Python Programming")

    def test_string_formatting(self):
        formatting = load_solution("05_strings", "03_string_formatting.py")
        self.assertEqual(formatting.formatted_examples()["total_cost"], "Total cost: $59.97")
        self.assertEqual(formatting.format_receipt()[-1], "Total: $1188.53")

    def test_string_iteration(self):
        iteration = load_solution("05_strings", "04_string_iteration.py")
        self.assertEqual(iteration.analyze_strings()["doubled_code"], "PPyytthhoonn")
        self.assertTrue(iteration.is_palindrome("level"))
        self.assertFalse(iteration.is_palindrome("python"))
