# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****


# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****


# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *

for n in range(0,5,2):
    print(('*'*(n+1)).rjust(n, '0'))

for n in range(6):
    print(('*'*(n+1)).rjust(6, ' '))

for n in range(11):
    if n <= 5:
        print(('*'*(n+1)))
    if n >=5:
        print(('*'*(11-n)).rjust(6, ' '))


# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.
# my_list = [2, 24, 12, 354, 233]
# for i in range(len(my_list) - 1): --range from 0 to 4
#     minimum = i
#     for j in range( i + 1, len(my_list)): 
#         if(my_list[j] < my_list[minimum]):
#             minimum = j
#             if(minimum != i):
#                 my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list)