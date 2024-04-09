# Exercise 1 : Hello World

print("Hello world\n" * 4)


# Exercise 2 : Some Math

print(99**3 * 8)


# Exercise 3 : What Is The Output ?

# 5 < 3 - False
# 3 == 3 - True
# 3 == "3" - False
# "3" > 3 - error, we can't compare str and int
# "Hello" == "hello" - False


# Exercise 4 : Your Computer Brand

computer_brand = "Asus"
print(f"I have a {computer_brand} computer")


# Exercise 5 : Your Information

name = "Artem"
age = 35
shoe_size = 8.5
info = f'For the last {age} years my name has been {name}. My shoe size is {shoe_size}'
print(info)

# Exercise 6 : A & B

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

if a > b:
    print("Hello World")


# Exercise 7 : Odd Or Even

n = int(input("Please enter a number: "))

if n % 2 == 0:
    print(f'Number {n} is even')
else:
    print(f'Number {n} is odd')


# Exercise 8 : What’s Your Name ?

username = input("Please enter your name: ")
my_name = "Artem"

if username == my_name:
    print("Cool name, dude!")
else:
    print("My hamster has the same name:)")


# Exercise 9 : Tall Enough To Ride A Roller Coaster

height = input("Enter your height in centimeters: ")

if int(height) < 145:
    print(f'So sorry, you need to grow some more to ride :(')
else:
    print(f"Congrats! You are tall enough to ride :)")




