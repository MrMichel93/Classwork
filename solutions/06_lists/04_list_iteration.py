"""Reference solution for the list iteration and processing exercise."""


def list_iteration_results():
    """Return results from processing each worksheet list with loops."""
    fruits = ["apple", "banana", "cherry", "date"]
    numbers = [10, 20, 30, 40, 50]
    doubled = []
    for number in numbers:
        doubled.append(number * 2)

    scores = [85, 92, 78, 90, 88]
    score_total = 0
    for score in scores:
        score_total += score

    long_words = 0
    for word in ["python", "java", "javascript", "ruby"]:
        if len(word) > 5:
            long_words += 1

    temperatures = [72, 68, 75, 82, 79, 73]
    highest_temperature = temperatures[0]
    for temperature in temperatures:
        if temperature > highest_temperature:
            highest_temperature = temperature

    lowercase_items = []
    for item in ["apple", "BANANA", "Cherry", "DATE"]:
        lowercase_items.append(item.lower())

    even_nums = []
    odd_nums = []
    for number in range(1, 11):
        if number % 2 == 0:
            even_nums.append(number)
        else:
            odd_nums.append(number)

    price_total = 0
    for price in [19.99, 24.50, 15.00, 32.99]:
        price_total += price

    grades = [88, 92, 79, 85, 97, 91]
    grade_labels = []
    for index, grade in enumerate(grades):
        grade_labels.append(f"Grade {index}: {grade}")

    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    people = []
    for name, age in zip(names, ages):
        people.append(f"{name} is {age} years old")

    return {
        "fruits": fruits,
        "doubled": doubled,
        "average_score": score_total / len(scores),
        "long_word_count": long_words,
        "highest_temperature": highest_temperature,
        "lowercase_items": lowercase_items,
        "even_nums": even_nums,
        "odd_nums": odd_nums,
        "total_with_tax": price_total * 1.08,
        "grade_labels": grade_labels,
        "people": people,
    }


if __name__ == "__main__":
    print(list_iteration_results())
