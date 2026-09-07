"""Student self-checks for topic 07 worksheets."""

from starter_tests._support import WorksheetTestCase


class TupleSetDictionarySelfChecks(WorksheetTestCase):
    def test_tuple_basics_output(self):
        worksheet = self.load("07_tuples_sets_dictionaries", "01_tuple_basics.py")
        self.assert_output_contains(
            worksheet, "(5,)", "(1, 2, 3, 4)",
            instruction="print the one-element tuple and concatenated tuple.",
        )

    def test_set_operations_output(self):
        worksheet = self.load("07_tuples_sets_dictionaries", "02_set_operations.py")
        self.assert_output_contains(
            worksheet, "orange", "lemon", "lime", "True",
            instruction="print union/intersection results and the apple membership check.",
        )

    def test_dictionary_basics_output(self):
        worksheet = self.load("07_tuples_sets_dictionaries", "03_dictionary_basics.py")
        self.assert_output_contains(
            worksheet, "Alice", "11th", "2.85", "True",
            instruction="print the updated student, $2.85 total, and apple-key membership result.",
        )

    def test_dictionary_methods_output(self):
        worksheet = self.load("07_tuples_sets_dictionaries", "04_dict_methods.py")
        self.assert_output_contains(
            worksheet, "Item: apples, Quantity: 50", "30", "grapes", "{}",
            instruction="iterate inventory, pop bananas, update it, and show the cleared backup.",
        )
