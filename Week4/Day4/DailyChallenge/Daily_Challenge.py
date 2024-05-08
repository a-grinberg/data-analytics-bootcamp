# What You Will Learn :
# OOP
# Modules

# Instructions :
# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.

# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# Implement a classmethod that returns a Text instance but with a text file:
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
# Now, use the provided the_stranger.txt file and try using the class you created above.

# Bonus:
# Create a class called TextModification that inherits from Text.
# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

string = 'A good book would sometimes cost as much as a good house'

class Text:
    def __init__(self, text=''):
        self.text = text
    
    def words_frecuency(self, word):
        return self.text.lower().split(' ').count(word.lower())
    
    def most_common_word(self):
        pass

    def get_unique_words(self):
        set_of_words = set(self.text.lower().split(' '))
        return list(set_of_words)
    
    @classmethod
    def from_file(cls, text_file):
        with open(text_file, 'r') as f:
            return cls(f.read())

class TextModification(Text):
    STOP_WORDS = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with']

    def get_text_without_punctuation(self):
        new_text = ''
        for word in self.text.split(' '):
            new_text += word.rstrip(',.!?:;"')+' '
        return new_text

    def get_text_without_stop_words(self):
        new_text = ''
        for word in self.text.split(' '):
            if word.rstrip(',.!?:;"').lower() not in __class__.STOP_WORDS:
                new_text += ' '+word
        return new_text
                

ex = TextModification()
stranger = ex.from_file('Week4/Day4/DailyChallenge/the_stranger.txt')
print(stranger.get_text_without_punctuation()[0:1000])
print(stranger.get_text_without_stop_words()[0:1000])

