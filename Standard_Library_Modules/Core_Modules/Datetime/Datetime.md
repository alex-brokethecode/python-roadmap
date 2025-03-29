# `datetime` Module

## Theory

The `datetime` module provides classes for working with dates and times. It's essential for handling time-related data in Python.

- `datetime.datetime`: Represents a specific date and time.
- `datetime.date`: Represents a date (year, month, day).
- `datetime.time`: Represents a time (hour, minute, second, microsecond).
- `datetime.timedelta`: Represents a duration, the difference between two dates or times.

### Formatting Dates and Times
- `strftime(format)`: Converts a `datetime` object to a string based on a format string.
- `strptime(date_string, format)`: Parses a date string into a `datetime` object based on a format string.

### Common Format Codes
- `%Y`: Year with century (e.g., 2023).
- `%y`: Year without century (e.g., 23).
- `%m`: Month (01-12).
- `%d`: Day (01-31).
- `%H`: Hour (00-23).
- `%M`: Minute (00-59).
- `%S`: Second (00-59).
- `%A`: Weekday (e.g., Monday).
- `%B`: Month name (e.g., January).

### Example

```python
import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

date_string = now.strftime("%A, %d %B %Y %H:%M:%S")
print("Formatted date and time:", date_string)

date_object = datetime.datetime.strptime("2023-10-27 10:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed date object:", date_object)

delta = datetime.timedelta(days=7)
future_date = now + delta
print("Date 7 days from now:", future_date)
```

## Exercises:

### Easy

1. **Current Date and Time:** Write a Python program that prints the current date and time in the format "YYYY-MM-DD HH:MM:SS".

### Medium

2. **Date Difference:** Write a Python program that takes two dates as input (in the format "YYYY-MM-DD") and calculates the number of days between them.

### Hard

3. **Weekday Calculation:** Write a Python program that takes a date as input (in the format "YYYY-MM-DD") and prints the day of the week (e.g., "Monday", "Tuesday", etc.).