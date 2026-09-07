"""Reference solution for the password validator exercise."""

password = "Secret123"
username = "user123"
confirm_password = "Secret123"


def validate_password(candidate, username_value, confirmation):
    """Return the checks required by the password validator exercise."""
    has_number = any(character.isdigit() for character in candidate)
    return {
        "length_is_good": len(candidate) >= 8,
        "has_number": has_number,
        "matches_username": candidate == username_value,
        "contains_password_word": "password" in candidate.lower(),
        "passwords_match": candidate == confirmation,
        "is_valid": len(candidate) >= 8 and candidate != username_value,
        "has_uppercase": candidate != candidate.lower(),
    }


if __name__ == "__main__":
    for label, passed in validate_password(password, username, confirm_password).items():
        print(f"{label.replace('_', ' ').title()}: {passed}")
