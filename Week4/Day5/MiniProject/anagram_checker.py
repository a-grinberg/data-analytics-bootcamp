class AnagramChecker:
    def __init__(self, file):
        with open(file, 'r') as f:
            self.word_list = f.read().split('\n')

    def is_valid_word(self, word):
        word = word.rstrip(' ').lstrip(' ')
        for l in word:
            if l.isalpha() == False:
                raise TypeError
        if word in self.word_list:
            return True
        return False


    def get_anagrams(self, user_word):
        anagrams = []
        for word in self.word_list:
            if len(word) == len(user_word):
                if sorted(list(word)) == sorted(list(user_word)) and word != user_word:
                    anagrams.append(word)
        return anagrams