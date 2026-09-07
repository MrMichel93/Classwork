"""Tests for tuple, set, and dictionary solutions."""

import unittest

from solution_loader import load_solution


class TupleSetDictionaryTests(unittest.TestCase):
    def test_tuple_basics(self):
        tuples = load_solution("07_tuples_sets_dictionaries", "01_tuple_basics.py")
        self.assertEqual(tuples.tuple_basics_results()["single"], (5,))
        self.assertEqual(tuples.tuple_basics_results()["second_point_y"], 2)

    def test_set_operations(self):
        sets = load_solution("07_tuples_sets_dictionaries", "02_set_operations.py")
        result = sets.set_operation_results()
        self.assertEqual(result["common_fruits"], {"orange"})
        self.assertEqual(result["symmetric_difference"], {1, 2, 4, 5})

    def test_dictionary_basics(self):
        dictionaries = load_solution("07_tuples_sets_dictionaries", "03_dictionary_basics.py")
        result = dictionaries.dictionary_basics_results()
        self.assertAlmostEqual(result["total"], 2.85)
        self.assertEqual(result["nested_city"], "NYC")

    def test_dictionary_methods(self):
        dictionaries = load_solution("07_tuples_sets_dictionaries", "04_dict_methods.py")
        result = dictionaries.dictionary_method_results()
        self.assertEqual(result["removed_bananas"], 30)
        self.assertEqual(result["backup"], {})
