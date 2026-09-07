"""Reference solution for the temperature conversion functions exercise."""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Celsius, then Celsius to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def print_all_temps(celsius):
    """Print a Celsius temperature in all three temperature scales."""
    print(f"Celsius: {celsius}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(celsius)}")
    print(f"Kelvin: {celsius_to_kelvin(celsius)}")


if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))
    print(celsius_to_fahrenheit(100))
    print(fahrenheit_to_celsius(98.6))
    print(celsius_to_kelvin(25))
    print(fahrenheit_to_kelvin(32))
    print_all_temps(25)
