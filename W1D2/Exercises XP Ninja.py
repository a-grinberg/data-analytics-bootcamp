# Exercise 3 : Outputs

# >>> 3 <= 3 < 9 - True
# >>> 3 == 3 == 3 True
# >>> bool(0) - True
# >>> bool(5 == "5") - False
# >>> bool(4 == 4) == bool("4" == "4") - True
# >>> bool(bool(None)) - False
# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10
#
# print("x is", x) - x is True
# print("y is", y) - Y is False
# print("a:", a) - 5
# print("b:", b) - 10


# Exercise 4 : How Many Characters In A Sentence ?

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
           Ut enim ad minim veniam, quis nostrud exercitation ullamco\
           laboris nisi ut aliquip ex ea commodo consequat.\
           Duis aute irure dolor in reprehenderit in voluptate velit\
           esse cillum dolore eu fugiat nulla pariatur.\
           Excepteur sint occaecat cupidatat non proident,\
           sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))


# Exercise 5: Longest Word Without A Specific Character

sentence = input("Input your sentence without the character “A”.")
old_len = 0

while "A" not in sentence.upper():
    if len(sentence) > old_len:
        old_len = len(sentence)
        print(f"Congratulations! Your sentence contains {old_len} letters")
    sentence = input("Input your sentence without the character “A”.")

print(f'Your sentence contain the character “A” :(')