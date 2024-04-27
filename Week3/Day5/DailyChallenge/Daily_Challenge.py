# Part 1 : Quizz :
# Answer the following questions
# What is a class?
# A Class is like an object constructor, or a pattern for creating objects. It defines attributes and methods that the objects of that class will have.
# What is an instance?
# instance is object, example or sample of class
# What is encapsulation?
# Encapsulation refers to bundling data, like attributes or methods together within a class. It hides the internal details and exposes only necessary interfaces
# What is inheritance?
# Inheritance allow to inherit properties and behaviors from an existing class (the parent class) to child class
# What is multiple inheritance?
# Multiple inheritance occurs when a class inherits from more than one parent class and allow to inherit properties and behaviors from each of them
# What is polymorphism?
# Polymorphism allows objects of different classes to be treated uniformly. It enables method calls to behave differently based on the object type.
# What is method resolution order or MRO?
# MRO determines the order in which Python looks for methods in a class hierarchy






# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random as r
class Deck:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
   
    def __init__(self) -> None:
        self.deck = self.get_deck()
    
    @classmethod
    def get_deck(cls):
        return [Card(suit, value) for suit in cls.SUITS for value in cls.VALUES]
    
    def shuffle(self):
        r.shuffle(self.deck)
        return self.deck

    def deal(self):
        return self.deck.pop()

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

deck = Deck()
print(deck.deal())