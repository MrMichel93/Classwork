"""Tests for list solutions."""

import unittest

from solution_loader import load_solution


class ListTests(unittest.TestCase):
    def test_list_basics(self):
        basics = load_solution("06_lists", "01_list_basics.py")
        self.assertEqual(basics.list_basics_results()["modified_numbers"], [1, 2, 10, 4, 5])
        self.assertEqual(basics.list_basics_results()["middle_grid_element"], 5)

    def test_list_methods(self):
        methods = load_solution("06_lists", "02_list_methods.py")
        result = methods.list_method_results()
        self.assertEqual(result["removed_color"], "yellow")
        self.assertEqual(result["index_of_nine"], 0)

    def test_list_operations(self):
        operations = load_solution("06_lists", "03_list_operations.py")
        self.assertEqual(operations.list_operation_results()["squares"][-1], 100)
        self.assertEqual(operations.list_operation_results()["index_two_to_six"], [2, 3, 4, 5, 6])

    def test_list_iteration(self):
        iteration = load_solution("06_lists", "04_list_iteration.py")
        result = iteration.list_iteration_results()
        self.assertEqual(result["highest_temperature"], 82)
        self.assertEqual(result["people"][0], "Alice is 25 years old")
