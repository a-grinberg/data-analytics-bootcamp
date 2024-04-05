#Exercise 1: Formula

# C = 50
# H = 30
# D = input("Enter a comma-separated string of numbers: ").split(",")

# Q = [int(((2*C*int(d)/H))**0.5) for d in D]

# print(Q)

#Exercise 2 : List Of Integers

lst1 = [3, 47, 5, 99, -80, 22, 97, 54, -23, 5, 7]
lst1_sorted = lst1[:]
lst1_sorted.sort(reverse=True)
print(*lst1)
print(*lst1_sorted)
print(sum(lst1))
print([lst1[0], lst1[-1]])
print([n for n in lst1 if n>50])
print([n for n in lst1 if n<10])
print([n**2 for n in lst1])

dist_lst = list(set(lst1))
print(dist_lst, len(dist_lst))
print(sum(lst1)/len(lst1))


#Exercise 3: Working On A Paragraph

text = """Python is considered to be one of the most efficient programming languages for data analysis.
          Using the Pandas library, Python provides fast, flexible, and expressive data structures
          designed to make working with data both easy and intuitive. This course will introduce
          the basics of the Python environment, including fundamental programming concepts such as control structures,
          functions, and data structures. At its core, this training will provide you a comprehensive toolset for working with data,
          including techniques for reading and writing diverse files, data cleaning and wrangling, analysis and visualization."""

print(len(text))

text_sentence = list(text.split("."))
text_words = list(text.split(" "))
    
print(len(text_sentence))
print(len(text_words))
print(len(set(list(text.split(" ")))))
print(len([l for l in text if l !=' ']))
print(len(text_words)/len(text_sentence))


# Exercise 4

string = list(input("Enter a text").split(" "))
dict_count = {}

for s in string:
    if s not in dict_count:
        dict_count[s] = string.count(s)
        print(f'{s}: {string.count(s)}')

