"""Tests for exception and file-handling solutions."""

import shutil
import unittest
from datetime import datetime
from pathlib import Path

from solution_loader import ROOT, load_solution


class ExceptionFileTests(unittest.TestCase):
    def setUp(self):
        self.work_dir = ROOT / "tests" / ".runtime_data"
        shutil.rmtree(self.work_dir, ignore_errors=True)
        self.work_dir.mkdir()

    def tearDown(self):
        shutil.rmtree(self.work_dir, ignore_errors=True)

    def test_exception_handling(self):
        exceptions = load_solution("08_exceptions_files", "01_exception_handling.py")
        self.assertEqual(exceptions.safe_divide(10, 2), 5)
        self.assertIsNone(exceptions.safe_divide(10, 0))
        with self.assertRaises(exceptions.InvalidAgeError):
            exceptions.validate_age(121)

    def test_file_reading(self):
        reading = load_solution("08_exceptions_files", "02_file_reading.py")
        sample = self.work_dir / "sample.txt"
        reading.create_sample_file(sample)
        self.assertEqual(reading.read_file_examples(sample)["first_line"], "Line 1: Hello World")
        self.assertIsNone(reading.safe_read_file(self.work_dir / "missing.txt"))
        numbers = self.work_dir / "numbers.txt"
        numbers.write_text("1\n2\n3\n", encoding="utf-8")
        self.assertEqual(reading.sum_numbers_in_file(numbers), 6)

    def test_file_writing(self):
        writing = load_solution("08_exceptions_files", "03_file_writing.py")
        output = self.work_dir / "output.txt"
        self.assertTrue(writing.write_list_to_file(output, [1, 2, 3]))
        self.assertEqual(output.read_text(encoding="utf-8"), "1\n2\n3\n")
        self.assertEqual(writing.append_after_reading(output, "four"), "1\n2\n3\n")
        log = self.work_dir / "log.txt"
        writing.append_log_message(log, "Finished", datetime(2026, 1, 2, 3, 4, 5))
        self.assertIn("2026-01-02 03:04:05: Finished", log.read_text(encoding="utf-8"))

    def test_json_files(self):
        json_files = load_solution("08_exceptions_files", "04_json_files.py")
        result = json_files.json_examples(self.work_dir)
        self.assertEqual(result["math_students"], ["Alice", "Bob"])
        student_path = self.work_dir / "student.json"
        self.assertEqual(json_files.update_json_value(student_path, "grade", "12th")["grade"], "12th")
        self.assertEqual(json_files.load_json(student_path)["grade"], "12th")
