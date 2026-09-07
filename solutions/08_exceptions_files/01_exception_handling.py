"""Reference solution for the exception handling exercise."""


class InvalidAgeError(ValueError):
    """Raised when an age is outside the valid range."""


def safe_divide(numerator, denominator):
    """Divide two values, returning ``None`` instead of dividing by zero."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None


def check_positive(number):
    """Raise an error for negative values and accept zero or positive values."""
    if number < 0:
        raise ValueError("Number must be positive")
    return "Number is valid"


def validate_age(age):
    """Return a valid age or raise ``InvalidAgeError``."""
    if not 0 <= age <= 120:
        raise InvalidAgeError("Age must be between 0 and 120")
    return age


def exception_examples():
    """Run the worksheet's examples and return their user-facing results."""
    results = {}
    try:
        10 / 0
    except ZeroDivisionError:
        results["division_by_zero"] = "Cannot divide by zero!"
    try:
        int("abc")
    except ValueError:
        results["invalid_integer"] = "Invalid number format!"
    try:
        [1, 2, 3][10]
    except IndexError:
        results["invalid_index"] = "Index out of range!"
    try:
        result = 20 / 4
    except ZeroDivisionError:
        results["successful_division"] = "Cannot divide by zero!"
    else:
        results["successful_division"] = result
    try:
        int("123")
    except ValueError:
        results["conversion"] = "Invalid number format!"
    finally:
        results["conversion_complete"] = "Conversion attempt complete"
    try:
        int("hello") + [1, 2, 3]
    except Exception as error:
        results["general_exception"] = f"{type(error).__name__}: {error}"
    return results


if __name__ == "__main__":
    print(exception_examples())
    print(safe_divide(10, 2), safe_divide(10, 0))
    try:
        check_positive(-5)
    except ValueError as error:
        print(error)
