"""Reference solution for the string formatting exercise."""


def formatted_examples():
    """Return each f-string example from the worksheet."""
    name = "Alice"
    age = 25
    price = 19.99
    quantity = 3
    pi = 3.14159265359
    first = "Python"
    second = "Programming"
    score = 87.5
    city = "Boston"
    number = 1234567
    temp_c = 25
    temp_f = (temp_c * 9 / 5) + 32
    sentence = "Hello    World"
    normalized_sentence = " ".join(sentence.split())
    border = "*" * (len(normalized_sentence) + 4)
    return {
        "introduction": f"My name is {name} and I am {age} years old",
        "total_cost": f"Total cost: ${price * quantity:.2f}",
        "rounded_pi": f"{pi:.2f}",
        "uppercase_words": f"{first.upper()} {second.upper()}",
        "percentage": f"{score:.2f}%",
        "person": f"{name} is {age} years old and lives in {city}.",
        "commas": f"{number:,}",
        "temperature": f"{temp_c}°C is equal to {temp_f:.1f}°F",
        "boxed_sentence": [border, f"* {normalized_sentence} *", border],
    }


def format_receipt():
    """Return a neatly formatted receipt for the bonus exercise."""
    items = [("Laptop", 999.99), ("Mouse", 25.50), ("Keyboard", 75.00)]
    subtotal = sum(price for _, price in items)
    tax = subtotal * 0.08
    lines = [f"Item {number}: {name} - ${price:.2f}" for number, (name, price) in enumerate(items, 1)]
    return lines + [
        f"Subtotal: ${subtotal:.2f}",
        f"Tax (8%): ${tax:.2f}",
        f"Total: ${subtotal + tax:.2f}",
    ]


if __name__ == "__main__":
    for value in formatted_examples().values():
        print(value)
    print(*format_receipt(), sep="\n")
