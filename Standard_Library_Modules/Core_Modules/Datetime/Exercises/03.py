# Weekday Calculation: Write a Python program that takes a date as input (in the format "YYYY-MM-DD")
# and prints the day of the week (e.g. "Monday", "Tuesday", etc.)

import datetime

# Parse input sting date to datetime
random_date = datetime.datetime.strptime('2025-08-03', '%Y-%m-%d')

# Print datetime object with format (Week day)
print(random_date.strftime('%A'))
