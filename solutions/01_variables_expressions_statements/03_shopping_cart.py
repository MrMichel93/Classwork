"""Reference solution for the shopping cart calculator exercise."""

item1_price = 15.99
item2_price = 23.50
item3_price = 8.75
tax_rate = 0.08
subtotal = item1_price + item2_price + item3_price
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount
money_left = 60.00 - total_cost
bulk_subtotal = 2 * item1_price + item2_price + 3 * item3_price
bulk_total_cost = bulk_subtotal * (1 + tax_rate)


def calculate_cart(prices, tax=0.08, starting_money=None):
    """Calculate subtotal, tax, total, and optional remaining money."""
    subtotal_value = sum(prices)
    total = subtotal_value * (1 + tax)
    result = {
        "subtotal": subtotal_value,
        "tax_amount": subtotal_value * tax,
        "total_cost": total,
    }
    if starting_money is not None:
        result["money_left"] = starting_money - total
    return result


if __name__ == "__main__":
    cart = calculate_cart(
        [item1_price, item2_price, item3_price], tax_rate, starting_money=60.00
    )
    for label, amount in cart.items():
        print(f"{label.replace('_', ' ').title()}: ${amount:.2f}")
    print(f"Bulk order total: ${bulk_total_cost:.2f}")
