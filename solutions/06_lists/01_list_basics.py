"""Reference solution for the list basics exercise."""


def list_basics_results():
    """Return the values produced while completing the list basics TODOs."""
    numbers = [1, 2, 3, 4, 5]
    original_numbers = numbers.copy()
    first_element = numbers[0]
    last_element = numbers[-1]
    length = len(numbers)
    numbers[2] = 10
    fruits = ["apple", "banana", "orange"]
    mixed = [42, 3.14, "hello", True]
    empty_list = []
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return {
        "numbers": original_numbers,
        "first_element": first_element,
        "last_element": last_element,
        "length": length,
        "modified_numbers": numbers,
        "second_fruit": fruits[1],
        "mixed": mixed,
        "empty_list": empty_list,
        "middle_grid_element": grid[1][1],
    }


if __name__ == "__main__":
    print(list_basics_results())
