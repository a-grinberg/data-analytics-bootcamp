# Exercise 1: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     #Your code starts HERE

# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)
# >>> str(c1)
# '5 dollars'
# >>> int(c1)
# 5
# >>> repr(c1)
# '5 dollars'
# >>> c1 + 5
# 10
# >>> c1 + c2
# 15
# >>> c1 
# 5 dollars
# >>> c1 += 5
# >>> c1
# 10 dollars
# >>> c1 += c2
# >>> c1
# 20 dollars
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        string = f"{self.amount} {self.currency}"
        if self.amount > 1:
            string += "s" 
        return string
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.amount + other.amount
        return self.amount + other
    
    def __radd__(self, other):
        if isinstance(other, type(self)):
            return self.amount + other.amount
        return self.amount + other
    
    def __int__(self):
        return self.amount
    
# Exercise 2: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file named exercise_one.py import and the function
# Hint: You can use the the following syntaxes:
# import module_name 
# OR 
# from module_name import function_name 
# OR 
# from module_name import function_name as fn 
# OR
# import module_name as mn

# See files func.py and exercise_one.py

# Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
from string import ascii_lowercase as lower, ascii_uppercase as upper
from random import randint as r

string1 = ''.join([(list(lower)+list(upper))[r(0,52)] for i in range(5)])
print(string1)

# Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import datetime, date
print(date.today())

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

next_year = datetime.now().year + 1
start = datetime.now()
stop = datetime(next_year, 1, 1, 00, 00, 00, 00)
print(f'the 1st of January is in {stop - start}')

# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

def get_minutes(birthdate):
    year, month, day = birthdate.split('/')
    birthdate = datetime(int(year), int(month), int(day), 00, 00, 00, 00)
    return (datetime.now()-birthdate).total_seconds() // 60

user_birthdate = input('Enter your date of birth (yyyy/mm/dd): ')

print(get_minutes(user_birthdate))

# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker

fake = Faker()
users = []

def generate_fake_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

for u in range(5):
    generate_fake_user()

for user in users:
    print(user)