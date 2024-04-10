# # Exercise 1 : Temperature Advice
# # Instructions
# # Create a function called get_random_temp().
# # This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# # Test your function to make sure it generates expected results.

# # Create a function called main().
# # Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# # Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# # Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# # below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# # between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# # between 16 and 23
# # between 24 and 32
# # between 32 and 40

# # Change the get_random_temp() function:
# # Add a parameter to the function, named ‘season’.
# # Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# # Now that we’ve changed get_random_temp(), let’s change the main() function:
# # Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# # Use the season as an argument when calling get_random_temp().


# from random import randint as r

# def get_random_temp(season):
#     temp = None
#     if season == 'winter':
#         temp = r(-10, 16)
#     elif season == 'spring':
#         temp = r(5, 22)
#     elif season == 'summer':
#         temp = r(23, 40)
#     else:
#         temp = r(10, 25)
#     return temp

# def main():
#     season = input('Enter a season: ')
#     temp = get_random_temp(season)
#     print(f'The temperature right now is {temp} degrees Celsius.')
#     if temp < 0 :
#         print(f'Brrr, that’s freezing! Wear some extra layers today')
#     elif 0 <= temp <= 16 :
#         print(f'Quite chilly! Don’t forget your coat')
#     elif 16 < temp <= 23 :
#         print(f'')
#     elif 24 <= temp < 32 :
#         print(f'')
#     else:
#         print(f'')

# main()

# # Bonus: Give the temperature as a floating-point number instead of an integer.
# # Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

# def get_random_temp(month):
#     temp = None
#     if 3 <= month <= 5:
#         temp = r(5, 22)
#     elif 6 <= month <= 8:
#         temp = r(23, 40)
#     elif 9 <= month <= 11:
#         temp = r(10, 25)
#     else:
#         temp = r(-10, 16)
#     return temp

# def main():
#     month = int(input('Enter a month: '))
#     temp = get_random_temp(month)
#     print(f'The temperature right now is {temp} degrees Celsius.')
#     if temp < 0 :
#         print(f'Brrr, that’s freezing! Wear some extra layers today')
#     elif 0 <= temp <= 16 :
#         print(f'Quite chilly! Don’t forget your coat')
#     elif 16 < temp <= 23 :
#         print(f'Warm')
#     elif 24 <= temp < 32 :
#         print(f'Warmer')
#     else:
#         print(f'Hot!')

# main()

# Exercise 2 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# def inform_user(correct, wrong):
#     return f'Number of right answers: {correct}. Number of wrong answers {wrong}'

# def sw_quiz(questions):
#     wrong_answers = {} # dict instead of list for bonus task
#     wrong = 0
#     correct = 0
#     for number, question in enumerate(questions):
#         print(question['question'])
#         user_answer = input('Enter your answer: ')
#         if user_answer != question['answer']:
#             wrong_answers[number] = user_answer
#             wrong += 1
#         else:
#             correct +=1
#     print(inform_user(correct, wrong))
#     for question, user_answer in wrong_answers.items():
#         print(f'Question: {questions[question]["question"]} Your answer: {user_answer} / Correct answer: {questions[question]["answer"]}')
#     new_quiz = input('Enter "yes" to play again or "no" to exit: ')
#     if new_quiz == 'yes':
#         sw_quiz(questions)

# sw_quiz(data)

# Exercise 3 : When Will I Retire ?
# Instructions
# The point of the exercise is to check if a person can retire depending on their age and their gender.
# Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).

# Create a function get_age(year, month, day)
# Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
# After calculating the age of a person, the function should return the age (the age is an integer).
# Create a function can_retire(gender, date_of_birth).
# It should call the get_age function (with what arguments?) in order to receive an age.
# Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
# Calculate. You may need to do a little more hard-coding here.
# Return True if the person can retire, and False if he/she can’t.
# Some Hints

# Ask for the user’s gender as “m” or “f”.
# Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
# Call can_retire to get a definite value for whether the person can or can’t retire.
# Display a message informing the user whether they can retire or not.
# As always, test your code to ensure it works.

from dateutil.relativedelta import relativedelta
from datetime import date # Hardcoding is a bad practice:)

def get_age(yy, mm, dd):
    now = date.today()
    date_of_birth = date(int(yy), int(mm), int(dd))
    age = relativedelta(now, date_of_birth).years
    return age

def can_retire(gender, date_of_birth):
    date = date_of_birth.split('/')
    age = get_age(*date)
    if (age > 67 and gender == 'm') or (age > 62 and gender == 'f'):
        return True
    return False

gender = input('Enter your gender f/m: ')
date_of_birth = input('Enter your date of birth yyyy/mm/dd: ')
print(can_retire(gender, date_of_birth))

# Exercise 4:
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:

# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)

# Hint: treating our number as a int or a str at different points in our code may be helpful

def function(x):
    return sum([int(str(x)*i) for i in range(1, 5)])
