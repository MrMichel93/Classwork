"""Student self-checks for topic 08 worksheets."""

import json
from pathlib import Path

from starter_tests._support import WorksheetTestCase, temporary_directory


class ExceptionFileSelfChecks(WorksheetTestCase):
    def test_exception_handling_functions(self):
        worksheet = self.load("08_exceptions_files", "01_exception_handling.py")
        self.assertEqual(self.require_callable(worksheet, "safe_divide")(10, 2), 5)
        self.assertIsNone(self.require_callable(worksheet, "safe_divide")(10, 0))
        with self.assertRaises(ValueError):
            self.require_callable(worksheet, "check_positive")(-1)

    def test_file_reading_function(self):
        worksheet = self.load("08_exceptions_files", "02_file_reading.py")
        safe_read_file = self.require_callable(worksheet, "safe_read_file")
        with temporary_directory("ap-csp-read-") as directory:
            sample = Path(directory) / "sample.txt"
            sample.write_text("Hello file!\n", encoding="utf-8")
            self.assertEqual(safe_read_file(sample), "Hello file!\n")
            self.assertIsNone(safe_read_file(Path(directory) / "missing.txt"))

    def test_file_writing_function(self):
        worksheet = self.load("08_exceptions_files", "03_file_writing.py")
        write_list_to_file = self.require_callable(worksheet, "write_list_to_file")
        with temporary_directory("ap-csp-write-") as directory:
            destination = Path(directory) / "numbers.txt"
            write_list_to_file(destination, [1, 2, 3])
            self.assertEqual(destination.read_text(encoding="utf-8"), "1\n2\n3\n")

    def test_json_saving_function(self):
        worksheet = self.load("08_exceptions_files", "04_json_files.py")
        save_to_json = self.require_callable(worksheet, "save_to_json")
        with temporary_directory("ap-csp-json-") as directory:
            destination = Path(directory) / "student.json"
            save_to_json(destination, {"name": "Alice", "grade": "10th"})
            self.assertEqual(
                json.loads(destination.read_text(encoding="utf-8"))["grade"], "10th"
            )
