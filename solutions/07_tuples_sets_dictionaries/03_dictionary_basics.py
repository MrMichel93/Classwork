"""Reference solution for the dictionary basics exercise."""


def dictionary_basics_results():
    """Return the results requested by the dictionary basics TODOs."""
    student = {"name": "Alice", "age": 15, "grade": "10th"}
    name = student["name"]
    age = student["age"]
    student["school"] = "Central High"
    after_school = student.copy()
    student["grade"] = "11th"

    prices = {"apple": 0.50, "banana": 0.30, "orange": 0.75}
    total = 3 * prices["apple"] + 2 * prices["banana"] + prices["orange"]
    mixed = {
        "name": "Bob",
        "age": 16,
        "scores": [90, 85, 88],
        "address": {"city": "NYC", "zip": "10001"},
    }
    return {
        "name": name,
        "age": age,
        "after_school": after_school,
        "student": student,
        "total": total,
        "grape_price": prices.get("grape", 0.00),
        "has_apple": "apple" in prices,
        "student_item_count": len(student),
        "nested_city": mixed["address"]["city"],
    }


if __name__ == "__main__":
    print(dictionary_basics_results())
