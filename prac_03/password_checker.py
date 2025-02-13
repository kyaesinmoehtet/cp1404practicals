MIN_LENGTH = 5
MAX_LENGTH = 15
REQUIRED_SPECIAL_CHAR = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def is_valid_password(password):
    """Check if the provided password is valid based on the defined rules."""
    # Check length
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        print(f"Password must be between {MIN_LENGTH} and {MAX_LENGTH} characters.")
        return False

    # Initialize counters
    has_lower = has_upper = has_digit = has_special = False

    # Check each character in the password
    for character in password:
        if character.islower():
            has_lower = True
        elif character.isupper():
            has_upper = True
        elif character.isdigit():
            has_digit = True
        elif character in SPECIAL_CHARACTERS:
            has_special = True

    # Display password requirements
    if not has_lower:
        print("Password must contain at least one lowercase character.")
    if not has_upper:
        print("Password must contain at least one uppercase character.")
    if not has_digit:
        print("Password must contain at least one number.")
    if REQUIRED_SPECIAL_CHAR and not has_special:
        print(f"Password must contain at least one special character: {SPECIAL_CHARACTERS}")

    # Determine if password is valid
    if has_lower and has_upper and has_digit and (not REQUIRED_SPECIAL_CHAR or has_special):
        return True
    return False


def main():
    """Main function to check password validity."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("    1 or more uppercase characters")
    print("    1 or more lowercase characters")
    print("    1 or more")

