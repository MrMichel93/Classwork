"""Reference solution for the number comparator exercise."""

num1 = 15
num2 = 20
num3 = 15


def compare_numbers(first, second, third):
    """Describe the relationships among three numbers."""
    if first == second:
        first_second = "The numbers are equal"
    elif first > second:
        first_second = "The first number is larger"
    else:
        first_second = "The second number is larger"
    at_least_two_equal = first == second or second == third or first == third
    return {
        "first_second_message": first_second,
        "difference": abs(first - second),
        "first_third_equal": first == third,
        "all_equal": first == second and second == third,
        "at_least_two_equal": at_least_two_equal,
        "second_between_first_and_third": min(first, third) <= second <= max(first, third),
        "first_is_even": first % 2 == 0,
    }


if __name__ == "__main__":
    for label, value in compare_numbers(num1, num2, num3).items():
        print(f"{label}: {value}")
