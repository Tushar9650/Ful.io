import re

def is_valid_contact_number(number):
    # Regular expression pattern to match valid contact numbers
    pattern = r'^(\+?1-?)?(\d{3}|\(\d{3}\)|\d{3}-|\+\d{3} ?)(\d{3}|\(\d{3}\)|\d{3}-|\+\d{3} ?)(\d{4}|\(\d{4}\)|\d{4})$'
    
    # Use the re.match function to check if the number matches the pattern
    if re.match(pattern, number):
        return True
    else:
        return False

# Test cases
numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for number in numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
