"""Reference solution for the age classifier exercise."""

age = 16
has_id = True


def classify_age(age_value):
    """Return the age-group message for an age."""
    if age_value < 0:
        return "Invalid age"
    if age_value <= 12:
        return "You are a child"
    if age_value <= 19:
        return "You are a teenager"
    if age_value <= 64:
        return "You are an adult"
    return "You are a senior citizen"


def age_messages(age_value, has_identification=False):
    """Return classification, eligible activities, and club entry message."""
    messages = [classify_age(age_value)]
    if age_value >= 16:
        messages.append("You can get a driver's license")
    if age_value >= 18:
        messages.append("You can vote")
    if age_value >= 21:
        messages.append("You are old enough for all adult activities")
    messages.append(
        "Can enter the club" if age_value >= 18 and has_identification
        else "Cannot enter the club"
    )
    return messages


if __name__ == "__main__":
    print(*age_messages(age, has_id), sep="\n")
