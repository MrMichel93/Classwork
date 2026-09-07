"""Reference solution for the loop accumulation exercise."""


def sum_one_to_one_hundred():
    """Return the sum from 1 through 100."""
    sum_total = 0
    for number in range(1, 101):
        sum_total += number
    return sum_total


def factorial_of_ten():
    """Return the product of 1 through 10."""
    product = 1
    for number in range(1, 11):
        product *= number
    return product


def count_evens_to_one_hundred():
    """Count even numbers from 1 through 100."""
    count = 0
    for number in range(1, 101):
        if number % 2 == 0:
            count += 1
    return count


def sum_odds_to_fifty():
    """Return the sum of odd numbers from 1 through 50."""
    total = 0
    for number in range(1, 51):
        if number % 2 != 0:
            total += number
    return total


def repeated_vowels():
    """Build the vowels repeated three times each."""
    result = ""
    for vowel in "aeiou":
        result += vowel * 3
    return result


def analyze_numbers(numbers):
    """Return loop-derived facts about a non-empty list of numbers."""
    max_value = numbers[0]
    min_value = numbers[0]
    total = 0
    greater_than_ten = 0
    even_numbers = []
    for number in numbers:
        total += number
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
        if number > 10:
            greater_than_ten += 1
        if number % 2 == 0:
            even_numbers.append(number)
    return {
        "maximum": max_value,
        "minimum": min_value,
        "average": total / len(numbers),
        "greater_than_ten": greater_than_ten,
        "even_numbers": even_numbers,
    }


def sum_of_squares_to_ten():
    """Return 1² + 2² + ... + 10²."""
    total = 0
    for number in range(1, 11):
        total += number * number
    return total


if __name__ == "__main__":
    sample_numbers = [5, 12, 8, 3, 19, 7, 15, 2]
    print(sum_one_to_one_hundred())
    print(factorial_of_ten())
    print(analyze_numbers(sample_numbers))
