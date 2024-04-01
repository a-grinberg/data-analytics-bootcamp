# Daily Challenge: Build Up A String
import random as r

# 1)
string = input("Please, input a string: ")

if len(string) == 10:
    print("Perfect string")
else:
    print("string not long enough" if len(string) < 10 else "string too long")

# 2)
print(string[0], string[-1])

# 3)

output = []

for c in string:
    output.append(c)
    print(''.join(output))

# 4)
r.shuffle(output)

print(''.join(output))

