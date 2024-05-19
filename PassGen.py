import secrets
import string

# Define variables
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
white_spaces = string.whitespace

pattern = letters + digits + special_chars + white_spaces

# Set password length
password_length = 24

def generate_password(length, pattern):
    """Generate a random password of specified length from the given pattern."""
    return ''.join(secrets.choice(pattern) for _ in range(length))

def meets_constraints(password, min_digits=2, min_special=1):
    """Check if the password meets the required constraints."""
    has_min_digits = sum(char in digits for char in password) >= min_digits
    has_min_special = any(char in special_chars for char in password)
    return has_min_digits and has_min_special

# Generate a password with constraints
while True:
    password = generate_password(password_length, pattern)
    if meets_constraints(password):
        break

print(password)
