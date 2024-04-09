#Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = {z[0]:z[1] for z in zip(keys, values)}
print(dict1)


#Exercise 2 : Cinemax

family = {}

names = input("Enter the names of the family members: ").split(" ")

for name in names:
    family[name] = int(input(f"Enter {name} age: "))

cost = {}

for name, age in family.items():
    if age <= 3:
        cost[name] = 0
    elif 3 < age <= 12:
        cost[name] = 10
    else:
        cost[name] = 15

print(*[f"{n}:{c}" for n, c in cost.items()], f"Total cost: {sum(cost.values())}")


#Exercise 3: Zara

brand = {'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona', 
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000, 
        'major_color': 
                    {
                    'France': 'blue', 
                    'Spain': 'red', 
                    'US': 'pink, green'
                    }}

brand['number_stores'] = 2
brand['country_creation'] = 'Spain'
brand.setdefault('international_competitors', 'Desigual')
brand.pop('creation_date')
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

more_on_zara = {'creation_date': 1975, 
                'number_stores': 10000}

brand.update(more_on_zara)
print(brand['number_stores'])


#Exercise 4 : Disney Characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users_A = {name:index for index, name in enumerate(users)}
disney_users_B = {index:name for index, name in enumerate(users)}
users.sort()
disney_users_C = {name:index for index, name in enumerate(users)}
disney_users_i = {name:index for index, name in enumerate(users) if 'i' in name}
disney_users_pm = {name:index for index, name in enumerate(users) if name[0].lower() in 'pm' }

print(disney_users_A)
print(disney_users_B)
print(disney_users_C)
print(disney_users_i)
print(disney_users_pm)