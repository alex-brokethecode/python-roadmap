# Find Email Addresses: Write a regular expression to find all email addresses in a given text

import re

text = "Contact us at 1K6oR@example.com or visit our website at https://www.example.com for more information. Optional email: admin@example.com"

match = re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

if match:
    print(match)
else:
    print('No email addresses found')
