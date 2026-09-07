"""Reference solution for the list methods exercise."""


def list_method_results():
    """Return results of the requested list-method operations."""
    colors = ["red", "blue", "green"]
    colors.append("yellow")
    after_append = colors.copy()
    colors.insert(1, "purple")
    after_insert = colors.copy()
    colors.remove("blue")
    after_remove = colors.copy()
    removed_color = colors.pop()

    numbers = [5, 2, 8, 1, 9, 3]
    numbers.sort()
    sorted_numbers = numbers.copy()
    numbers.reverse()
    reversed_numbers = numbers.copy()

    repeated_fives = [5, 2, 5, 8, 5, 1]
    animals = ["cat", "dog", "bird"]
    animal_copy = animals.copy()
    animal_copy.append("fish")
    extended = [1, 2, 3]
    extended.extend([4, 5, 6])
    cleared = ["one", "two"]
    cleared.clear()
    return {
        "after_append": after_append,
        "after_insert": after_insert,
        "after_remove": after_remove,
        "removed_color": removed_color,
        "remaining_colors": colors,
        "sorted_numbers": sorted_numbers,
        "reversed_numbers": reversed_numbers,
        "eight_is_present": 8 in numbers,
        "index_of_nine": numbers.index(9),
        "five_count": repeated_fives.count(5),
        "animals": animals,
        "animal_copy": animal_copy,
        "extended": extended,
        "cleared": cleared,
    }


if __name__ == "__main__":
    print(list_method_results())
