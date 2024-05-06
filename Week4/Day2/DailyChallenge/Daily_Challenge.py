# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles


class Circle:
    def __init__(self, radius = None, diameter = None) -> None:
        self._radius = diameter/2 if radius == None else radius
        self._diameter = radius * 2 if diameter == None else diameter

    def get_area(self):
        PI = 3.14
        return PI * (self._radius ** 2)
    
    def __add__(self, value):
        new_circle_area = self.get_area() + value.get_area()
        PI = 3.14
        radius = (new_circle_area / PI)**0.5
        return Circle(radius=radius)
        
    def put_circle(self, lst):
        lst.append(self)
        sorted(lst, key=lambda x: x.get_area())
        return lst  

    def __str__(self):
        return f'Radius: {self._radius} \nDiameter: {self._diameter}'

    def __eq__(self, value):
        if self.get_area() == value.get_area():
            return True
        return False
    
    def __gt__(self, value):
        if self.get_area() > value.get_area():
            return True
        return False
    
    def __lt__(self, value):
        if self.get_area() < value.get_area():
            return True
        return False
    
circle1 = Circle(radius=2)
circle2 = Circle(diameter=5)
circle3 = circle2+circle1
lst1 = []
circle3.put_circle(lst1)
circle1.put_circle(lst1)
circle2.put_circle(lst1)
