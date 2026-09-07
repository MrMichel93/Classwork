"""Reference solution for the grade checker exercise."""

score = 85


def grade_for(score_value):
    """Return a letter grade, or ``Invalid score`` outside 0 through 100."""
    if score_value < 0 or score_value > 100:
        return "Invalid score"
    if score_value >= 90:
        return "A"
    if score_value >= 80:
        return "B"
    if score_value >= 70:
        return "C"
    if score_value >= 60:
        return "D"
    return "F"


def grade_messages(score_value):
    """Return the messages the worksheet program would print."""
    grade = grade_for(score_value)
    if grade == "Invalid score":
        return ["Invalid score"]
    messages = [f"Grade: {grade}"]
    if score_value == 100:
        messages.append("Perfect score!")
    return messages


if __name__ == "__main__":
    print(*grade_messages(score), sep="\n")
