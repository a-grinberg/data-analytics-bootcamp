# Count Occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.


string = input('Enter a string: ')
character = input('Enter a character: ')

def count_occurence(string, character):
    count = 0
    for char in string:
        if char == character:
            count += 1
    return count

print(count_occurence(string, character))