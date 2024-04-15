# Exercise 1 : Geometry
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.
from math import pi

class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_area(self):
        return pi * self.radius**2
    
    def get_definition():
        print('A circle is a plane figure bounded by one curved line, and such that all straight lines drawn from a certain point within it to the bounding line, are equal.')


# Exercise 2 : Custom List Class
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
from random import randint

class MyList:
    def __init__(self, list_of_letters):
        self.lst = list_of_letters

    def get_reversed_list(self):
        return self.lst[::-1]

    def get_sorted_list(self):
        return sorted(self.lst)
    
    def get_random_list(self):
        return [randint(0, 1000) for n in range(len(self.lst))]