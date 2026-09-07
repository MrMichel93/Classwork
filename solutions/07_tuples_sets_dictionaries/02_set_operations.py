"""Reference solution for the set operations exercise."""


def set_operation_results():
    """Return the results requested by the set operation TODOs."""
    fruits = {"apple", "banana", "orange"}
    fruits.add("grape")
    after_grape = fruits.copy()
    fruits.add("apple")
    after_duplicate = fruits.copy()
    citrus = {"orange", "lemon", "lime"}
    all_fruits = fruits.union(citrus)
    common_fruits = fruits.intersection(citrus)
    fruit_difference = fruits.difference(citrus)
    fruits.remove("banana")
    duplicate_free_numbers = set([1, 2, 2, 3, 3, 3, 4])
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    return {
        "after_grape": after_grape,
        "after_duplicate": after_duplicate,
        "all_fruits": all_fruits,
        "common_fruits": common_fruits,
        "fruit_difference": fruit_difference,
        "after_banana_removed": fruits,
        "has_apple": "apple" in fruits,
        "duplicate_free_numbers": duplicate_free_numbers,
        "fruit_count": len(fruits),
        "symmetric_difference": set1.symmetric_difference(set2),
    }


if __name__ == "__main__":
    print(set_operation_results())
