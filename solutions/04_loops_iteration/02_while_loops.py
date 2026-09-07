"""Reference solution for the while loops exercise."""


def count_up_to_ten():
    """Return numbers from 1 through 10 using a while loop."""
    counter = 1
    values = []
    while counter <= 10:
        values.append(counter)
        counter += 1
    return values


def countdown():
    """Return numbers from 10 down to 1 using a while loop."""
    value = 10
    values = []
    while value >= 1:
        values.append(value)
        value -= 1
    return values


def sum_one_to_twenty():
    """Return the sum from 1 through 20 using a while loop."""
    total = 0
    current = 1
    while current <= 20:
        total += current
        current += 1
    return total


def doubles_through_one_thousand():
    """Return powers of two through the first value greater than 1000."""
    number = 1
    values = []
    while number <= 1000:
        number *= 2
        values.append(number)
    return values


def two_to_tenth_power():
    """Calculate 2 to the tenth power with repeated multiplication."""
    power = 1
    exponent = 0
    while exponent < 10:
        power *= 2
        exponent += 1
    return power


def find_secret_number(secret_number=7, first_guess=1):
    """Simulate increasing guesses until the secret number is found."""
    guess = first_guess
    guesses = 1
    while guess != secret_number:
        guess += 1
        guesses += 1
    return guess, guesses


def halve_until_less_than_one(start=100):
    """Return halved values and the number of divisions."""
    num = start
    values = []
    divisions = 0
    while num >= 1:
        num /= 2
        values.append(num)
        divisions += 1
    return values, divisions


if __name__ == "__main__":
    print(count_up_to_ten())
    print(countdown())
    print(sum_one_to_twenty())
    print(doubles_through_one_thousand())
    print(two_to_tenth_power())
    print(find_secret_number())
