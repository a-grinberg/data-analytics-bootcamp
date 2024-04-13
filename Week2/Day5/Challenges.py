# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

def insert_item(lst, index, item):
    lst.insert(index, item)
    return lst


# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

def count_spaces(string):
    count = 0
    for char in string:
        if char == ' ':
            count += 1
    return count


# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.
import string

def count_letters(str1):
    lower = 0
    upper = 0
    for char in str1:
        if char in string.ascii_lowercase:
            lower += 1
        if char in string.ascii_uppercase:
            upper += 1    
    return (lower, upper)


# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12

def sum_of_array(lst):
    sum_lst = 0
    for number in lst:
        sum_lst += number
    return sum_lst

# Exercise 5
# Instructions
# Write a function to find the max number in a list

def find_max(lst):
    max = 0
    for number in lst:
        if number > max:
            max = number
    return number



# Exercise 6
# Instructions
# Write a function that returns factorial of a number
def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):
def list_count(lst, element):
    count = 0
    for e in lst:
        if e == element:
            count += 1
    return count


# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

def norm(lst):
    return sum([x**2 for x in lst])**0.5


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_mono(lst):
    if lst[0] < lst[-1]:
        for index in range(1, len(lst)):
            if lst[index] < lst[index-1]:
                return False
    else:
        for index in range(1, len(lst)):
            if lst[index] > lst[index-1]:
                return False
    return True



# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def longest_word(lst):
    l_word = ''
    for word in lst:
        if len(word) > len(l_word):
            l_word = word
    return l_word


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def merge_list(lst):
    integers = []
    strings = []
    for element in lst:
        if isinstance(element, int):
            integers.append(element)
        else:
            strings.append(element)
    return (integers, strings)

# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

def sum_over_k(sentence,k):
    return len(list(filter(lambda x: len(x) > k, sentence.split(' '))))

# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

def dict_avg(dict_of_numbers):
    lst_values = dict_of_numbers.values()
    return sum(lst_values)/len(lst_values)


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

def common_div(a, b):
    min = a if a < b else b
    return [x for x in range(1, min+1) if a % x == 0 and b % x == 0]


# Exercise 16
# Instructions
# Write a function that test if a number is prime:

def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

def weird_print(lst):
    return list(filter(lambda x: lst[x] % 2 == 0 and x % 2 == 0, range(len(lst))))


# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

def type_count(**kwargs):
    types = {}
    for k in kwargs.values():
        t = str(type(k)).split(' ')[-1].strip("'>")
        if t in types:
            types[t] +=1
        else:
            types[t] =1
    return types

# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.
def mimics_split(string, divider):
    lst = []
    word = ''
    for char in string:
        if char != divider:
            word += char
        else:
            lst.append(word)
            word = ''
    lst.append(word)
    return lst

# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"

def format_string(password):
    return '*'*len(password)


# Exercise 2
assert count_spaces('Hel lo worl d') == 3

# Exercise 3
assert count_letters('HeLLo PyThOn') == (5, 6)

# Exercise 4
assert sum_of_array([1,5,4,2]) == 12

# Exercise 5
assert find_max([0,1,3,50]) == 50

# Exercise 6
assert factorial(4) == 24

# Exercise 7
assert list_count(['a','a','t','o'],'a') == 2

# Exercise 8
assert norm([1,2,2]) == 3

# Exercise 9
assert is_mono([7,6,5,5,2,0]) == True
assert is_mono([2,3,3,3]) == True
assert is_mono([1,2,0,4]) == False

# Exercise 10
assert longest_word(['Hello', 'python', 'dictionary', 'list', 'loop' ]) == 'dictionary'

# Exercise 11
assert merge_list(['Hello', 77, 'python', 5, 'list', 92]) == ([77, 5, 92], ['Hello', 'python', 'list'])

# Exercise 12
assert is_palindrome('radar') == True

assert is_palindrome('John') == False

# Exercise 13
sentence = 'Do or do not there is no try'
k = 2
assert sum_over_k(sentence,k) == 3

# Exercise 14
assert dict_avg({'a': 1,'b':2,'c':8,'d': 1}) == 3

# Excercise 15
assert common_div(10,20) == [1,2,5,10]

# Excercise 16
assert is_prime(11) == True
assert is_prime(12) == False

# Excercise 17
assert weird_print([1,2,2,3,4,5]) == [2,4]

# Excercise 18
assert type_count(a=1,b='string',c=1.0,d=True,e=False) == {'int': 1, 'str':1 , 'float':1, 'bool':2}

# Exercise 19
assert mimics_split('Hello/python/and/world', '/') == ['Hello', 'python', 'and', 'world']

# Exercise 20
assert format_string('mypassword') == "**********"