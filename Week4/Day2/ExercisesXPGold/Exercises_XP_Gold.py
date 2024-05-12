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

# Exercise 5: Python Password Generator
# Instructions
# Create a Python program that will generate a good password for you.

# Program flow:

# Ask the user to type in the number of characters that the password should have (password length) – between 6 and 30 characters.
# Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which will continue to ask the user for an input until they enter a valid one.

# Generate a password with the required length.

# Print the password with a user-friendly message which reminds the user to keep the password in a safe place!

# Rules for the validity of the password

# Each password should contain:
# At least 1 digit (0-9)
# At least 1 lower-case character (a-z)
# At least 1 upper-case character (A-Z)
# At least 1 special character (eg. !, @, #, $, %, ^, _, …)
# Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.

# Create a test function first!

# Do the following steps 100 times, with different password lengths:
# Generate a password.
# Test the password to ensure that:
# it fulfills all the requirements above (eg. it has at least one digit, etc.)
# it has the specified length.