"""Reference solution for the string basics exercise."""

message = "Hello, Python!"
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
word = "Python"
programming = "programming"


def describe_message(text):
    """Return the indexing and slicing results requested by the worksheet."""
    return {
        "first_character": text[0],
        "last_character": text[-1],
        "length": len(text),
        "first_five": text[:5],
        "last_seven": text[-7:],
        "every_other": text[::2],
        "reversed": text[::-1],
    }


def middle_two_characters(text):
    """Return the two characters centered in an even-length word."""
    middle = len(text) // 2
    return text[middle - 1:middle + 1]


def vowels_from_programming():
    """Extract the vowels at the worksheet's requested positions."""
    return programming[2] + programming[5] + programming[6] + programming[9]


if __name__ == "__main__":
    print(describe_message(message))
    print(full_name)
    print(middle_two_characters(word))
    print(vowels_from_programming())
