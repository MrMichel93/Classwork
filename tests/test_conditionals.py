"""Tests for conditional solutions."""

import unittest

from solution_loader import load_solution


class ConditionalTests(unittest.TestCase):
    def test_grade_checker(self):
        grades = load_solution("02_conditionals", "01_grade_checker.py")
        self.assertEqual(grades.grade_for(100), "A")
        self.assertEqual(grades.grade_messages(100), ["Grade: A", "Perfect score!"])
        self.assertEqual(grades.grade_for(-1), "Invalid score")

    def test_age_classifier(self):
        classifier = load_solution("02_conditionals", "02_age_classifier.py")
        self.assertEqual(classifier.classify_age(13), "You are a teenager")
        self.assertIn("Can enter the club", classifier.age_messages(21, True))

    def test_number_comparator(self):
        comparator = load_solution("02_conditionals", "03_number_comparator.py")
        result = comparator.compare_numbers(15, 20, 15)
        self.assertEqual(result["difference"], 5)
        self.assertTrue(result["at_least_two_equal"])

    def test_password_validator(self):
        validator = load_solution("02_conditionals", "04_password_validator.py")
        result = validator.validate_password("Secret123", "user123", "Secret123")
        self.assertTrue(result["is_valid"])
        self.assertTrue(result["has_number"])
