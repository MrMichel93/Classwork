"""Reference solution for the string methods exercise."""

text = "python programming"
phrase = "  Hello World  "
sentence = "apple,banana,orange,grape"
list_of_words = ["I", "love", "Python"]


def string_method_results(value=text):
    """Return results from the string methods demonstrated in the worksheet."""
    return {
        "uppercase": value.upper(),
        "title_case": value.title(),
        "stripped_phrase": phrase.strip(),
        "starts_with_python": value.startswith("python"),
        "ends_with_ing": value.endswith("ing"),
        "programming_position": value.find("programming"),
        "python_three": value.replace("python", "Python 3"),
        "fruit_list": sentence.split(","),
        "joined_words": " ".join(list_of_words),
        "o_count": value.count("o"),
    }


def case_transformations(value="PyThOn ProGramMinG"):
    """Return lowercase, uppercase, and title-case forms."""
    return value.lower(), value.upper(), value.title()


if __name__ == "__main__":
    print(string_method_results())
    print(case_transformations())
