# Exercise 1: Birthday Look-Up, Exercise 2: Birthdays Advanced, Exercise 3: Add Your Own Birthday

birthdays = {'Nick': '1995/10/01', 'Phill': '1989/02/23', 'Kate': '2001/04/17', 'Angela': '1992/08/09', 'Zack': '2003/11/24'}

persons_name = input("Enter a person's name: ")
persons_birthday = input("Enter a person's birthday in the format 'YYYY/MM/DD': ")
birthdays[persons_name] = persons_birthday

print('You can look up the birthdays of the people in the list!')
print(*birthdays.keys())
name = input("Enter a person's name: ")
birthday = birthdays.get(name)
print(f"{name}'s birthday {birthday}")


# Exercise 4: Fruit Shop

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

items_str = ''

for item, price in items.items():
    items_str += f'{item}: {price},'

print(items_str)

items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

print({item: int(value["price"]) * int(value["stock"]) for item, value in items.items()})
 