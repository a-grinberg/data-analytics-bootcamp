# Exercise 1 : Cars

cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(',')

print(len(cars))
cars.sort(reverse=True)
print(cars)
print(len([car for car in cars if 'o' in car]))
print(len([car for car in cars if 'i' not in car]))
cars2 = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars2 = list(set(cars2))

print(', '.join(cars2), f'Total: {len(cars2)}')
cars2.sort()
print(cars2)