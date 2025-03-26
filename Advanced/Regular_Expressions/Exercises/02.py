# Validate Phone Numbers: Write a regular expression to validate phone numbers in a specific format. (e.g., xxx-xxx-xxxx)

import re


def validate_phone(phone_number: str) -> bool:
    pattern = r'^\d{3}-\d{3}-\d{4}$'

    return bool(re.match(pattern, phone_number))


test1 = '123-456-7890'
test2 = '(51) 123456'

print(validate_phone(test1))
print(validate_phone(test2))
