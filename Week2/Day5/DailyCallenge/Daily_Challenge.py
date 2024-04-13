# Challenge 1 : Sorting
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

def sorting_words(string):
    string_lst = string.split(',')
    string_lst.sort()
    return ','.join(string_lst)



# Challenge 2 : Longest Word
# Instructions
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

def longest_word(sentence):
    l_word = ''
    for word in sentence.split(' '):
        if len(word) > len(l_word):
            l_word = word
    return l_word


# Challenge 1 : Sorting
assert sorting_words('without,hello,bag,world') == 'bag,hello,without,world'

# Challenge 2 : Longest word
assert longest_word("Margaret's toy is a pretty doll.") == "Margaret's"
assert longest_word("A thing of beauty is a joy forever.") == "forever."
assert longest_word("Forgetfulness is by all means powerless!") == "Forgetfulness"