"""Reference solution for the file writing exercise."""

from datetime import datetime
from pathlib import Path


def write_list_to_file(filename, items):
    """Write one item per line and return whether the write succeeded."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for item in items:
                file.write(f"{item}\n")
    except OSError:
        return False
    return True


def write_lines(filename, lines):
    """Write several lines at once, adding newlines when needed."""
    prepared_lines = [line if line.endswith("\n") else f"{line}\n" for line in lines]
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(prepared_lines)


def append_after_reading(filename, line):
    """Use r+ mode to read a file and then append a line."""
    with open(filename, "r+", encoding="utf-8") as file:
        original_content = file.read()
        file.write(line if line.endswith("\n") else f"{line}\n")
    return original_content


def write_person(filename, person):
    """Write dictionary entries in a readable ``key: value`` form."""
    with open(filename, "w", encoding="utf-8") as file:
        for key, value in person.items():
            file.write(f"{key}: {value}\n")


def append_log_message(filename, message, timestamp=None):
    """Append a timestamped message to a caller-supplied log path."""
    moment = timestamp or datetime.now()
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{moment.isoformat(sep=' ', timespec='seconds')}: {message}\n")


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        directory_path = Path(directory)
        output_path = directory_path / "output.txt"
        output_path.write_text("This is the first line\n", encoding="utf-8")
        with output_path.open("a", encoding="utf-8") as file:
            file.write("This is an appended line\n")
        print(output_path.read_text(encoding="utf-8"))
        write_lines(directory_path / "poem.txt", ["Roses are red", "Violets are blue", "Python is fun"])
        write_list_to_file(directory_path / "fruits.txt", ["apple", "banana", "orange"])
        write_list_to_file(directory_path / "numbers.txt", [1, 2, 3, 4, 5])
        write_person(directory_path / "person.txt", {"name": "Alice", "age": 25, "city": "Boston"})
        append_after_reading(output_path, "A final line")
