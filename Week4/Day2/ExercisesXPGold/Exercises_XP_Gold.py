# Exercise 1 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.
from datetime import date, datetime

def get_date(dates):
    next_holiday = None
    for d in sorted(dates.keys()):
        if date.fromisoformat(d) >= date.today():
            next_holiday = d
            break
    print(next_holiday)
    print(f'The next holiday is {dates[next_holiday]} in {datetime.fromisoformat(next_holiday) - datetime.now()}')

holidays = {'2024-04-23': 'Pessah',
            '2024-05-14': 'Independence Day' ,
            '2024-06-12': 'Feast of Shavuot' ,
            '2024-10-03': 'Rosh Hashanah',
            '2024-10-12': 'Yom Kippur',
            '2024-10-17': 'Day of Sukkot' ,
            '2024-10-24': 'Simchat Torah'
            }

get_date(holidays)

# Exercise 3 : Regular Expression #1
# Instructions
# Hint: Use the RegEx (module)

# Use the regular expression module to extract numbers from a string.
import re

def return_numbers(string):
    return ''.join(re.findall(r'[0-9]', string))

assert return_numbers('k5k3q2g5z6x9bn') == '532569'

# Exercise 4 : Regular Expression #2
# Instructions
# Hint: Use the RegEx (module)

# Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
# The name should contain only letters.
# The name should contain only one space.
# The first letter of each name should be upper cased.



def validate_name(name):
    if re.match(r'[A-Z][a-z]*[\s][A-Z][a-z]*', name):
        return True
    return False

name = input('Enter your name: ')
print(validate_name(name))
