# Challenge 1
 
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

print([n*number for n in range(1, length+1)])

# Chalenge 2

word = input("Enter a word: ")

print(''.join([l for i, l in enumerate(word) if l !=word[i-1]]))