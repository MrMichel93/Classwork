"""Student self-checks for topic 06 worksheets."""

from starter_tests._support import WorksheetTestCase


class ListSelfChecks(WorksheetTestCase):
    def test_list_basics_output(self):
        worksheet = self.load("06_lists", "01_list_basics.py")
        self.assert_output_contains(
            worksheet, "[1, 2, 10, 4, 5]", "banana",
            instruction="print the modified number list and the second fruit.",
        )

    def test_list_methods_output(self):
        worksheet = self.load("06_lists", "02_list_methods.py")
        self.assert_output_contains(
            worksheet, "yellow", "[9, 8, 5, 3, 2, 1]", "0",
            instruction="print the popped color, reversed sorted numbers, and index of 9.",
        )

    def test_list_operations_output(self):
        worksheet = self.load("06_lists", "03_list_operations.py")
        self.assert_output_contains(
            worksheet, "[0, 1, 2, 3, 4]", "[7, 8, 9]", "45", "100",
            instruction="print sliced lists, their sum, and the final square number.",
        )

    def test_list_iteration_output(self):
        worksheet = self.load("06_lists", "04_list_iteration.py")
        self.assert_output_contains(
            worksheet, "[20, 40, 60, 80, 100]", "82", "[2, 4, 6, 8, 10]",
            instruction="print doubled numbers, the highest temperature, and the even-number list.",
        )
