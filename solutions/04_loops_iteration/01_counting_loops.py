"""Reference solution for the counting loops exercise."""


def count_up_to_ten():
    """Return numbers from 1 through 10."""
    numbers = []
    for number in range(1, 11):
        numbers.append(number)
    return numbers


def count_from_zero():
    """Return numbers from 0 through 9."""
    return [number for number in range(10)]


def even_numbers_to_twenty():
    """Return even numbers from 2 through 20."""
    return [number for number in range(2, 21, 2)]


def countdown():
    """Return a countdown from 10 to 1."""
    return [number for number in range(10, 0, -1)]


def sum_one_to_one_hundred():
    """Calculate the sum from 1 through 100 using a loop."""
    total = 0
    for number in range(1, 101):
        total += number
    return total


def multiplication_table(number=5, through=10):
    """Return formatted multiplication facts."""
    return [f"{number} x {factor} = {number * factor}" for factor in range(1, through + 1)]


def count_divisible_by_three():
    """Count numbers from 1 through 50 divisible by three."""
    count = 0
    for number in range(1, 51):
        if number % 3 == 0:
            count += 1
    return count


def first_square_numbers(count=10):
    """Return the first chosen number of square numbers."""
    return [number * number for number in range(1, count + 1)]


def multiplication_grid(size=5):
    """Return a 1-by-1 through size-by-size multiplication grid."""
    return [[row * column for column in range(1, size + 1)] for row in range(1, size + 1)]


if __name__ == "__main__":
    print(*count_up_to_ten(), sep="\n")
    print(sum_one_to_one_hundred())
    print(*multiplication_table(), sep="\n")
