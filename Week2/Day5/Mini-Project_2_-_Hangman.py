# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

body_parts = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
user_word = ['*' for _ in range(len(word))]

while (len(body_parts) != 0) and (''.join(user_word) != word):
    user_letter = input("Enter a letter: ")
    if user_letter in word:
        for index, letter in enumerate(word):
            if letter == user_letter:
                user_word[index] = letter
    else:
        body_parts.pop()
    print(''.join(user_word))


if ''.join(user_word) == word:
    print('You won!')
else:
    print('You lose!')