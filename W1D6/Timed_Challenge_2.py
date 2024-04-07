x = int(input('Enter the Number:')) 

dividers = []
for number in range(1,x):
    if x % number == 0:
        dividers.append(number)

print(True if sum(dividers) == x else False)