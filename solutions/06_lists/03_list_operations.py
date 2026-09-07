"""Reference solution for the list operations exercise."""


def list_operation_results():
    """Return the requested list operation and slicing results."""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = list1 + list2
    repeated = [1, 2, 3] * 3
    numbers = list(range(10))
    squares = []
    for number in range(1, 11):
        squares.append(number * number)
    return {
        "concatenated": list3,
        "repeated": repeated,
        "first_five": numbers[:5],
        "last_three": numbers[-3:],
        "every_other": numbers[::2],
        "index_two_to_six": numbers[2:7],
        "reversed": numbers[::-1],
        "sum": sum(numbers),
        "maximum": max(numbers),
        "minimum": min(numbers),
        "squares": squares,
        "evens_to_twenty": [number for number in range(21) if number % 2 == 0],
    }


if __name__ == "__main__":
    print(list_operation_results())
