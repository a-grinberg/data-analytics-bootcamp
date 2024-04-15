# Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat('Felix', 2)
cat2 = Cat('Luna', 5)
cat3 = Cat('Jack', 3)

def oldest_cat(*args):
    o_cat = args[0]
    for cat in args:
        if cat.age > o_cat.age:
            o_cat = cat
    return f'The oldest cat is {o_cat.name}, and is {o_cat.age} years old.'

print(oldest_cat(cat1, cat2, cat3))

# Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height*2} cm high!')
    

davids_dog = Dog('Rex', 50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)


# Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for s in self.lyrics:
            print(s)
    
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        for a in self.animals:
            print(a)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        sorted_animals = {1:self.animals[0]}
        count = 1
        for r in range(1, len(self.animals)):
            if self.animals[r].startswith(self.animals[r-1][0]):
                if isinstance(sorted_animals[count], str):
                    sorted_animals[count] = [sorted_animals[count], self.animals[r]]
                else:
                    sorted_animals[count].append(self.animals[r])
            else:
                count += 1
                sorted_animals[count] = self.animals[r]
        return sorted_animals

    def get_groups(self):
        animals = self.sort_animals()
        for animal in animals.values():
            print(animal)      


ramat_gan_safari = Zoo('ramat_gan_safari')
Ape = ramat_gan_safari.add_animal('Ape')
Baboon = ramat_gan_safari.add_animal('Baboon')
Bear = ramat_gan_safari.add_animal('Bear')
cat = ramat_gan_safari.add_animal('Cat')
cougar = ramat_gan_safari.add_animal('Cougar')
camel = ramat_gan_safari.add_animal('Camel')
eel = ramat_gan_safari.add_animal('Eel')
emu = ramat_gan_safari.add_animal('Emu')

ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Bear')
assert ramat_gan_safari.sort_animals() == {1: 'Ape', 2: ['Baboon', 'Bear'], 3: ['Camel', 'Cat', 'Cougar'], 4: ['Eel', 'Emu']}
ramat_gan_safari.get_groups()