# Harder Daily Challenge
# Notice : solve this exercise using a lambda function.

# Ask a user for the following inputs 5 times:
# Name (string)
# Age (int)
# Score (int)
# Build a list of tuples using these inputs, each tuple should contain a name, age and score.
# Sort the list by the following priority Name > Age > Score.
# If the following tuples are given as input to the script:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# Note : The lambda function will not print but sort

users_lst = [('Jony', '17', '91'), ('John', '20', '90'), ('Json', '21', '85'), ('Jony', '17', '93'), ('Tom', '19', '80')]

# for ask in range(5):
#     answer = (
#             input('Enter a name: '),
#             int(input('Enter an age: ')),
#              int(input('Enter a score: '))
#             )
#     users_lst.append(answer)

sorted(users_lst, key=lambda x: (x[0], x[1], x[2]))
print(users_lst)