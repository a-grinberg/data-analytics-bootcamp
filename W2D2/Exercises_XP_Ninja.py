# Exercise 1 : Box Of Stars

def box_printer(*args):
    longest_word = max([len(word) for word in args])
    words = ['* ' + word + ' '*(longest_word-len(word)) + ' *' for word in args]
    print('*'*(longest_word+4))
    for w in words:
        print(w)
    print('*'*(longest_word+4))

box_printer("Hello", "World", "in", "reallylongword", "a", "frame")