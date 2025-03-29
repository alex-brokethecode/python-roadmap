# Current Date and Time: Write a Python program that prints the current date and time
# in format "YYYY-MM-DD HH:MM:SS".

import datetime

now = datetime.datetime.now()
formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_now)
