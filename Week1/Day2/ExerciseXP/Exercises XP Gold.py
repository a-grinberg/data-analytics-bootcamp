# Exercise 1 : Hello World-I Love Python

print(f'Hello world ' * 4, f'I love python ' * 4)


# Exercise 2 : What Is The Season ?

month = int(input("Enter the month number:"))

while month < 1 or month > 12:
    print("Enter the number from 1 to 12")
    month = int(input("Enter the month number:"))

if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
else:
    print("Winter")

