#Exercise 1 : Set

my_fav_numbers = {7, 5, 17, 88}
my_fav_numbers.add(9)
my_fav_numbers.add(10)
my_fav_numbers.remove(10)
friend_fav_numbers = set((9, 7, 66, 22, 15))
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2: Tuple
#No. Tuple is unmutable type of data.

#Exercise 3: List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print(len(basket))
basket.clear()
print(basket)


# Exercise 4: Floats


lst1 = [r/10 for r in range(10, 60, 5)]
print(lst1)
# We also can use the linspace function from the NumPy.


# Exercise 5: For Loop

for n in range(1, 21):
    print(n)

for n in range(1, 21):
    if n % 2 == 0:
        print(n)


#Exercise 6 : While Loop
name = ''
while name != "Artem":
    name = input("Please, enter your name: ")


# Exercise 7: Favorite Fruits

fruits = input("Enter the names of your favorite fruits separated by a space: ").split(' ')
fruit = input("Enter the name of the fruit: ")
print(f"You chose one of your favorite fruits! Enjoy!" if fruit in fruit else "You chose a new fruit. I hope you enjoy")


# # Exercise 8: Who Ordered A Pizza ?
topping = ''
cost = 10
pizza = []
while True:
    topping = input("Enter the name of pizza topping: ")
    if topping == "quit":
        break
    pizza.append(topping)
    cost += 2.5

print(f"Your pizza with {', '.join(pizza)}. Cost: {cost}")

# Exercise 9: Cinemax

number_of_persons = int(input("How many tickets do you need? "))
cost = 0

for n in range(number_of_persons):
    person_age = int(input(f"Enter the age of person {n+1}: "))
    if person_age <= 3:
        continue
    elif 3 < person_age <= 12:
        cost += 10
    else:
        cost += 15
print(f"Total cost: {cost}")

teens = ["Jane", "Scott", "Lin", "Alex", "John"]
teens2 = teens[:]

for t in teens2:
    age = int(input(f"Enter your age {t}: "))
    if age < 16 or age > 21:
        teens.remove(t)

print(teens)

# Exercise 10 : Sandwich Orders

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while len(sandwich_orders) != 0:
    finished_sandwiches.insert(0, sandwich_orders.pop())

print(*[f'I made your tuna {s}\n' for s in finished_sandwiches])