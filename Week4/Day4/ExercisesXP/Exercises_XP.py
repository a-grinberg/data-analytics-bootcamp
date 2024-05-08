# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

from random import choices
def get_words_from_file(file):
    try:
        with open(file, 'r') as f:
            return f.read().split('\n')
    except:
        print('Something went wrong!')

file = 'C:/DI_Bootcamp/data-analytics-bootcamp/Week4/Day4/ExercisesXP/sowpods.txt'
list_of_words = get_words_from_file(file)

def get_random_sentence(length):
    sentence_lst = choices(list_of_words, k=length)
    return ' '.join(sentence_lst).lower()


def main():
    print('This program creates a sentence using random words from the given file.')
    length = input('Enter a sentence length (integer from 2 to 20): ')
    try:
        if 2 <= int(length) <= 20:
            sentence = get_random_sentence(int(length))
            print(sentence)
        else:
            raise ValueError('Value must be between 2 and 20.')
    except:
        print('Something went wrong!')

if __name__ == '__main__':
    main()


# Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
salary = data['company']['employee']['payable']['salary']
data['company']['employee']['birth_date'] = '1995/03/21'
data = json.dumps(data)
with open('Week4/Day4/ExercisesXP/data.json', 'w') as f:
    f.write(data)