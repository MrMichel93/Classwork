"""Tests for loop and iteration solutions."""

import unittest

from solution_loader import load_solution


class LoopIterationTests(unittest.TestCase):
    def test_counting_loops(self):
        loops = load_solution("04_loops_iteration", "01_counting_loops.py")
        self.assertEqual(loops.sum_one_to_one_hundred(), 5050)
        self.assertEqual(loops.multiplication_table()[4], "5 x 5 = 25")

    def test_while_loops(self):
        loops = load_solution("04_loops_iteration", "02_while_loops.py")
        self.assertEqual(loops.two_to_tenth_power(), 1024)
        self.assertEqual(loops.find_secret_number(), (7, 7))

    def test_loop_patterns(self):
        patterns = load_solution("04_loops_iteration", "03_loop_patterns.py")
        self.assertEqual(patterns.right_triangle(), ["*", "**", "***", "****", "*****"])
        self.assertEqual(patterns.bordered_square()[2], "*   *")

    def test_loop_accumulation(self):
        accumulation = load_solution("04_loops_iteration", "04_loop_accumulation.py")
        self.assertEqual(accumulation.factorial_of_ten(), 3628800)
        self.assertEqual(accumulation.analyze_numbers([5, 12, 8])["even_numbers"], [12, 8])
