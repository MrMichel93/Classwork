"""Reference solution for the file reading exercise."""

from pathlib import Path

SAMPLE_LINES = [
    "Line 1: Hello World\n",
    "Line 2: Python is fun\n",
    "Line 3: File handling is easy\n",
]


def create_sample_file(filename):
    """Create the sample text file at a caller-supplied path."""
    Path(filename).write_text("".join(SAMPLE_LINES), encoding="utf-8")


def safe_read_file(filename):
    """Read and return a file's content, or ``None`` when it is missing."""
    try:
        with open(filename, encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def read_file_examples(filename):
    """Return complete, line-by-line, first-line, list, and partial reads."""
    path = Path(filename)
    with path.open(encoding="utf-8") as file:
        whole_file = file.read()
    with path.open(encoding="utf-8") as file:
        stripped_lines = [line.strip() for line in file]
    with path.open(encoding="utf-8") as file:
        first_line = file.readline().strip()
    with path.open(encoding="utf-8") as file:
        lines = file.readlines()
    with path.open(encoding="utf-8") as file:
        first_ten_characters = file.read(10)
    return {
        "whole_file": whole_file,
        "stripped_lines": stripped_lines,
        "first_line": first_line,
        "lines": lines,
        "first_ten_characters": first_ten_characters,
    }


def sum_numbers_in_file(filename):
    """Return the sum of one integer stored on each line."""
    total = 0
    with open(filename, encoding="utf-8") as file:
        for line in file:
            total += int(line.strip())
    return total


def count_words_in_file(filename):
    """Count whitespace-separated words in a text file."""
    with open(filename, encoding="utf-8") as file:
        return sum(len(line.split()) for line in file)


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        sample_path = Path(directory) / "sample.txt"
        numbers_path = Path(directory) / "numbers.txt"
        create_sample_file(sample_path)
        numbers_path.write_text("1\n2\n3\n4\n5\n", encoding="utf-8")
        print(read_file_examples(sample_path))
        print(safe_read_file(Path(directory) / "missing.txt"))
        print(sum_numbers_in_file(numbers_path))
        print(count_words_in_file(sample_path))
