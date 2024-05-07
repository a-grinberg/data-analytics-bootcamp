# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module. Take a look at the googletrans module

from googletrans import Translator

# French words
french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translation_dict = {}
translator = Translator()

for word in french_words:
    translation = translator.translate(word, src='fr', dest='en')
    translation_dict[word] = translation.text

print(translation_dict)