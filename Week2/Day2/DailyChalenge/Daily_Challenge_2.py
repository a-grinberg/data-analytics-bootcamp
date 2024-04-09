import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

list_of_numbers = list(filter(lambda x: x < target_number, list_of_numbers))
list_of_couples = []

for number in list_of_numbers:
    for number2 in list_of_numbers:
        if number + number2 == target_number:
            list_of_couples.append((number, number2))

print(len(list_of_couples))
print(len(set(list_of_numbers)))