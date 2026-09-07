"""Reference solution for the string manipulation functions exercise."""


def make_uppercase(text):
    """Return text in uppercase."""
    return text.upper()


def make_lowercase(text):
    """Return text in lowercase."""
    return text.lower()


def get_length(text):
    """Return the number of characters in text."""
    return len(text)


def add_exclamation(text):
    """Return text followed by an exclamation mark."""
    return text + "!"


def repeat_string(text, times):
    """Return text repeated a chosen number of times."""
    return text * times


def get_initials(first_name, last_name):
    """Return uppercase initials with periods."""
    return f"{first_name[0].upper()}.{last_name[0].upper()}."


def count_vowels(text):
    """Count vowels in text without regard to case."""
    return sum(character in "aeiou" for character in text.lower())


def reverse_string(text):
    """Return text in reverse order."""
    return text[::-1]


if __name__ == "__main__":
    print(make_uppercase("hello world"))
    print(get_length("Python Programming"))
    print(repeat_string("Python", 3))
    print(get_initials("Ada", "Lovelace"))
    print(count_vowels("Python Programming"))
    print(reverse_string("Python"))
