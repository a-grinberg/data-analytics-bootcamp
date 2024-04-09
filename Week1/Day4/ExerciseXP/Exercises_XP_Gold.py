# Exercise 1: Concatenate Lists

lst1 = [2, 5, 6, 4, 6, 8]
lst2 = [3, 7, 9, 1]

lst1.extend(lst2)


# Exercise 2: Range Of Numbers

for n in range(1500, 2500):
    if n%(5*7) == 0:
        print(n)


# Exercise 3: Check The Index

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

username = input("Enter your name: ")

if username in names:
    print(names.index(username))

# Exercise 4: Greatest Number

g_number = 0
for i in range(3):
    number = int(input(f"Input the number {i+1}: "))
    if number > g_number:
        g_number = number

print(f"The greatest number is: {g_number}")


# Exercise 5: The Alphabet

import string

alphabet = string.ascii_lowercase

for l in alphabet:
    if l in ["a", "e", "i", "o", "u", "y"]:
        print(f"The letter {l} is vowel.")
    else:    
        print(f"The letter {l} is consonant.")


# Exercise 6: Words And Letters

words = []
for i in range(7):
    word = input("Enter a word: ")
    words.append(word)

letter = input("Enter a single character: ")

for w in words:
    if letter in w:
        print(w.index(letter))
    else:
        print(f"Hello {w}")

# Exercise 7:

numbers_lst = [n for n in range(1, 1000001)]

max_n = max(numbers_lst)
min_n = min(numbers_lst)
sum_n = sum(numbers_lst)
print(min_n, max_n, sum_n)

# Exercise 8 : List And Tuple

numbers_lst = list(input("Enter a sequence of comma-separated numbers: ").split(", "))
numbers_tpl = tuple(numbers_lst)

print(numbers_lst, numbers_tpl)


# Exercise 9 : Random Number

import random

number = int(input("Input a number from 1 to 9"))
r_number = random.randint(1,9)

if number == r_number:
    print("Winner!")
else:
    print("Better luck next time!")





