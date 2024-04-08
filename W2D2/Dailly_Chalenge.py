# Daily Challenge: Solve The Matrix

string = '7iiTsxh%?i #sM $a #t%^r!'

message = [[string[i+n] if string[i+n].isalpha() else ' ' for i in range(0, len(string), 3)] for n in range(3)]
print(''.join(''.join(m) for m in message))