"""Reference solution for the simple calculator exercise."""

number1 = 10
number2 = 5
sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2
remainder = number1 % number2
power = number1**number2
author_name = "Reference Solution"


def calculate(first_number, second_number):
    """Return the arithmetic results for two numbers."""
    return {
        "sum": first_number + second_number,
        "difference": first_number - second_number,
        "product": first_number * second_number,
        "quotient": first_number / second_number,
        "remainder": first_number % second_number,
        "power": first_number**second_number,
    }


def display_calculation(first_number, second_number):
    """Print calculator results in a readable format."""
    for name, value in calculate(first_number, second_number).items():
        print(f"{name.title()}: {value}")


if __name__ == "__main__":
    display_calculation(number1, number2)
    print(f"Calculator completed by {author_name}")
