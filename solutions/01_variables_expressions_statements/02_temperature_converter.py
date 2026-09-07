"""Reference solution for the temperature converter exercise."""

temp_celsius = 25.0
temp_fahrenheit = (temp_celsius * 9 / 5) + 32
temp_kelvin = temp_celsius + 273.15
body_temp_f = 98.6
body_temp_c = (body_temp_f - 32) * 5 / 9
freezing_to_boiling_fahrenheit = (100 * 9 / 5 + 32) - (0 * 9 / 5 + 32)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


if __name__ == "__main__":
    print(f"Celsius: {temp_celsius}")
    print(f"Fahrenheit: {temp_fahrenheit}")
    print(f"Kelvin: {temp_kelvin}")
    print(f"Body temperature: {body_temp_f}°F / {body_temp_c:.1f}°C")
    print(f"Freezing-to-boiling range: {freezing_to_boiling_fahrenheit}°F")
