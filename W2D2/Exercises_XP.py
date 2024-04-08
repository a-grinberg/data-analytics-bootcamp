# Exercise 1 : What Are You Learning ?

def display_message():
    print("We are learning Python!")

display_message()


# Exercise 2: What’s Your Favorite Book ?

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")


# Exercise 3 : Some Geography

def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")

describe_city('Madrid', 'Spain')

# Exercise 4 : Random

from random import randint

number = int(input('Enter the number betwen 1 and 100: '))

def compare_numbers(number):
    number2 = randint(1,100)
    print("Success" if number == number2 else "Fail", f'Number 1: {number}, Number 2: {number2}')

compare_numbers(number)

# Exercise 5 : Let’s Create Some Personalized Shirts !

def make_shirt(size='L', text='I love Python'):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt()
make_shirt('M')
make_shirt('S', 'Hello World!')


# Exercise 6 : Magicians …

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians():
    print(*[magician_names])

def make_great():
    for index, name in enumerate(magician_names):
        magician_names[index] = 'the Great ' + name

make_great()
show_magicians()