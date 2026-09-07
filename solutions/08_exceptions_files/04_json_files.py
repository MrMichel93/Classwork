"""Reference solution for the JSON files exercise."""

import json
from pathlib import Path


def save_to_json(filename, data):
    """Save a dictionary or list as formatted JSON and return success."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError:
        return False
    return True


def load_json(filename):
    """Load and return JSON data from a caller-supplied path."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def update_json_value(filename, key, value):
    """Update one top-level value in a JSON object and save it."""
    data = load_json(filename)
    data[key] = value
    save_to_json(filename, data)
    return data


def json_examples(directory):
    """Complete the file-based TODOs in a caller-supplied directory."""
    directory_path = Path(directory)
    student = {
        "name": "Bob",
        "age": 16,
        "grade": "11th",
        "subjects": ["Math", "Science", "English"],
    }
    student_path = directory_path / "student.json"
    save_to_json(student_path, student)
    loaded_student = load_json(student_path)

    numbers_json = json.dumps([1, 2, 3, 4, 5])
    city = json.loads('{"city": "New York", "population": 8000000}')

    students = [
        {"name": "Alice", "age": 15, "grade": "10th"},
        {"name": "Bob", "age": 16, "grade": "11th"},
        {"name": "Charlie", "age": 17, "grade": "12th"},
    ]
    students_path = directory_path / "students.json"
    save_to_json(students_path, students)
    student_names = [item["name"] for item in load_json(students_path)]

    try:
        json.loads('{"name": "Alice", age: 25}')
    except json.JSONDecodeError:
        invalid_json_message = "Invalid JSON format"

    school = {
        "school": "Central High",
        "classes": {"Math": ["Alice", "Bob"], "Science": ["Charlie", "Diana"]},
    }
    school_path = directory_path / "school.json"
    save_to_json(school_path, school)
    math_students = load_json(school_path)["classes"]["Math"]
    return {
        "student": loaded_student,
        "numbers_json": numbers_json,
        "city": city,
        "student_names": student_names,
        "invalid_json_message": invalid_json_message,
        "math_students": math_students,
    }


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        print(json_examples(directory))
