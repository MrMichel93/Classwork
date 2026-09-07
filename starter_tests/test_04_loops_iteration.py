"""Student self-checks for topic 04 worksheets."""

from starter_tests._support import WorksheetTestCase


class LoopIterationSelfChecks(WorksheetTestCase):
    def test_counting_loops_output(self):
        worksheet = self.load("04_loops_iteration", "01_counting_loops.py")
        self.assert_output_contains(
            worksheet, "5050", "5 x 10 = 50",
            instruction="print the 1-to-100 sum and all entries through 5 x 10 = 50.",
        )

    def test_while_loops_output(self):
        worksheet = self.load("04_loops_iteration", "02_while_loops.py")
        self.assert_output_contains(
            worksheet, "210", "1024", "Found it", "7",
            instruction="print the 1-to-20 sum, 2^10, and the successful secret-number search.",
        )

    def test_loop_patterns_output(self):
        worksheet = self.load("04_loops_iteration", "03_loop_patterns.py")
        self.assert_output_contains(
            worksheet, "*****", "12345", "*   *", "*-*-*-*-*-",
            instruction="print the required triangle, numbered triangle, bordered square, and alternating pattern.",
        )

    def test_loop_accumulation_output(self):
        worksheet = self.load("04_loops_iteration", "04_loop_accumulation.py")
        self.assert_output_contains(
            worksheet, "5050", "3628800", "aeiouaeiouaeiou", "[12, 8, 2]",
            instruction="print the sum, factorial, repeated vowels, and even-number list.",
        )
