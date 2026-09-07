"""Helpers for loading numeric lesson filenames in tests."""

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_solution(topic, filename):
    """Load one reference solution module from its file path."""
    path = ROOT / "solutions" / topic / filename
    module_name = f"solution_{topic.replace('-', '_')}_{filename.replace('.', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
