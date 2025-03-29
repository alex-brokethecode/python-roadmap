# Date Difference: Write a Python program that takes two dates as input (in the format "YYYY-MM-DD")
# and calculates the number of days between them.

import datetime

# Input dates
now = '2025-03-28'
future = '2025-08-03'

# Parse string to datetime objects
now = datetime.datetime.strptime(now, '%Y-%m-%d')
future = datetime.datetime.strptime(future, '%Y-%m-%d')

# Calculate difference
delta = future - now  # datetime.timedelta
print(delta.days)
