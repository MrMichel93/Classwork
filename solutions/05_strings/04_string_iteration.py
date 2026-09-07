"""Reference solution for the string iteration and analysis exercise."""


def analyze_strings():
    """Return the loop-based string analysis results from the worksheet."""
    text = "Hello, World!"
    vowels = 0
    for character in text:
        if character in "aeiouAEIOU":
            vowels += 1

    message = "programming"
    m_count = 0
    for character in message:
        if character == "m":
            m_count += 1

    sentence = "Learning Python is fun"
    spaces = 0
    for character in sentence:
        if character == " ":
            spaces += 1

    data = "abc123xyz"
    digits = 0
    for character in data:
        if character.isdigit():
            digits += 1

    consonants = ""
    for character in "Hello World":
        if character.lower() not in "aeiou" and character != " ":
            consonants += character

    doubled_code = ""
    for character in "Python":
        doubled_code += character * 2

    uppercase = lowercase = other = 0
    for character in text:
        if character.isupper():
            uppercase += 1
        elif character.islower():
            lowercase += 1
        else:
            other += 1

    has_digit = False
    for character in "Secret123":
        if character.isdigit():
            has_digit = True

    return {
        "characters": list("Python"),
        "vowel_count": vowels,
        "m_count": m_count,
        "space_count": spaces,
        "digit_count": digits,
        "consonants": consonants,
        "doubled_code": doubled_code,
        "uppercase_count": uppercase,
        "lowercase_count": lowercase,
        "other_count": other,
        "password_has_digit": has_digit,
    }


def is_palindrome(word):
    """Check matching characters from both ends using a loop."""
    for index in range(len(word) // 2):
        if word[index] != word[-(index + 1)]:
            return False
    return True


if __name__ == "__main__":
    print(*analyze_strings()["characters"], sep="\n")
    print(analyze_strings())
    print(is_palindrome("level"))
