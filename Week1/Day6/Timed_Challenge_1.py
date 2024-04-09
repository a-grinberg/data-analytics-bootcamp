# Reverse The Sentence

text = list(input("Enter a sentence: ").split(' '))
text.sort(reverse=True)
print(' '.join(text))