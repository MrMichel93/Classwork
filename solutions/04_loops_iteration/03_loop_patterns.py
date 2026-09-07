"""Reference solution for the loop patterns exercise."""


def asterisk_row():
    """Return one row of ten asterisks."""
    return "*" * 10


def asterisk_rectangle(rows=5, columns=10):
    """Return rows of asterisks for a rectangle."""
    return ["*" * columns for _ in range(rows)]


def right_triangle(size=5):
    """Return a right triangle made of asterisks."""
    return ["*" * row for row in range(1, size + 1)]


def number_triangle(size=5):
    """Return lines of increasing digits."""
    return ["".join(str(number) for number in range(1, row + 1)) for row in range(1, size + 1)]


def bordered_square(size=5):
    """Return a square with asterisks around its border."""
    rows = []
    for row in range(size):
        rows.append("*" * size if row in (0, size - 1) else "*" + " " * (size - 2) + "*")
    return rows


def countdown_pattern(start=5):
    """Return the worksheet's shrinking countdown pattern."""
    return ["".join(str(number) for number in range(start, end - 1, -1)) for end in range(1, start + 1)]


def alternating_characters(length=10):
    """Return alternating asterisks and hyphens."""
    return "".join("*" if index % 2 == 0 else "-" for index in range(length))


def pyramid(size=5):
    """Return a centered asterisk pyramid."""
    return [" " * (size - row) + "*" * (2 * row - 1) for row in range(1, size + 1)]


if __name__ == "__main__":
    print(asterisk_row())
    print(*asterisk_rectangle(), sep="\n")
    print(*right_triangle(), sep="\n")
    print(*bordered_square(), sep="\n")
