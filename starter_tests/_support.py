"""Helpers shared by the student-facing worksheet checks."""

import ast
import contextlib
import importlib.util
import io
import os
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIRECTORY = ROOT / "starter_tests"


@dataclass
class LoadedWorksheet:
    """A worksheet module and the output it produced while loading."""

    module: object
    output: str
    path: Path


def load_worksheet(topic: str, filename: str) -> LoadedWorksheet:
    """Load one original worksheet in an isolated working directory."""

    path = ROOT / topic / filename
    module_name = f"starter_check_{topic}_{filename.replace('.', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Could not prepare {path.relative_to(ROOT)} for checking.")

    module = importlib.util.module_from_spec(spec)
    output = io.StringIO()
    original_directory = Path.cwd()
    try:
        with temporary_directory("ap-csp-self-check-") as work_dir:
            os.chdir(work_dir)
            with contextlib.redirect_stdout(output):
                spec.loader.exec_module(module)
    except Exception as error:
        raise AssertionError(
            f"Could not run {path.relative_to(ROOT)}: {type(error).__name__}: {error}. "
            "Fix the worksheet's TODO code so it runs without an exception."
        ) from error
    finally:
        os.chdir(original_directory)

    return LoadedWorksheet(module, output.getvalue(), path)


def temporary_directory(prefix: str) -> tempfile.TemporaryDirectory:
    """Create temporary test data inside starter_tests, never in course folders."""

    return tempfile.TemporaryDirectory(dir=RUNTIME_DIRECTORY, prefix=prefix)


class WorksheetTestCase(unittest.TestCase):
    """Assertions that turn incomplete worksheet work into actionable feedback."""

    def load(self, topic: str, filename: str) -> LoadedWorksheet:
        return load_worksheet(topic, filename)

    def require_callable(self, worksheet: LoadedWorksheet, name: str):
        value = getattr(worksheet.module, name, None)
        self.assertTrue(
            callable(value),
            f"{worksheet.path.relative_to(ROOT)} is incomplete: define the `{name}` "
            "function named in its TODO instructions.",
        )
        return value

    def require_class(self, worksheet: LoadedWorksheet, name: str):
        value = getattr(worksheet.module, name, None)
        self.assertTrue(
            isinstance(value, type),
            f"{worksheet.path.relative_to(ROOT)} is incomplete: define the `{name}` "
            "class named in its TODO instructions.",
        )
        return value

    def require_method(self, class_, method_name: str, worksheet: LoadedWorksheet):
        value = getattr(class_, method_name, None)
        self.assertTrue(
            callable(value),
            f"{worksheet.path.relative_to(ROOT)} is incomplete: add the "
            f"`{method_name}` method to `{class_.__name__}`.",
        )
        return value

    def assert_output_contains(
        self, worksheet: LoadedWorksheet, *expected: str, instruction: str
    ) -> None:
        missing = [text for text in expected if text not in worksheet.output]
        self.assertFalse(
            missing,
            f"{worksheet.path.relative_to(ROOT)} is incomplete: {instruction} "
            f"Missing output: {', '.join(repr(text) for text in missing)}. "
            f"Captured output: {worksheet.output[:300]!r}",
        )

    def assert_conditional_structure(
        self, worksheet: LoadedWorksheet, instruction: str
    ) -> None:
        tree = ast.parse(worksheet.path.read_text(encoding="utf-8"))
        if_count = sum(isinstance(node, ast.If) for node in ast.walk(tree))
        self.assertGreaterEqual(
            if_count,
            2,
            f"{worksheet.path.relative_to(ROOT)} is incomplete: {instruction}",
        )
