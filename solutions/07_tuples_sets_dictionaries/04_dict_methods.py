"""Reference solution for the dictionary methods exercise."""


def dictionary_method_results():
    """Return the results requested by the dictionary-method TODOs."""
    inventory = {"apples": 50, "bananas": 30, "oranges": 40}
    keys = list(inventory.keys())
    values = list(inventory.values())
    items = list(inventory.items())
    item_lines = []
    for key, value in inventory.items():
        item_lines.append(f"Item: {key}, Quantity: {value}")
    removed_bananas = inventory.pop("bananas")
    after_removal = inventory.copy()
    inventory.update({"grapes": 25, "pears": 15})
    mangoes = inventory.setdefault("mangoes", 0)
    backup = inventory.copy()
    backup.clear()
    field_names = ["name", "age", "city"]
    field_values = ["Alice", 25, "Boston"]
    person = dict(zip(field_names, field_values))
    return {
        "keys": keys,
        "values": values,
        "items": items,
        "item_lines": item_lines,
        "removed_bananas": removed_bananas,
        "after_removal": after_removal,
        "inventory": inventory,
        "mangoes": mangoes,
        "backup": backup,
        "person": person,
    }


if __name__ == "__main__":
    print(dictionary_method_results())
