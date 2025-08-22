#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.name)   # Buddy
print(dog1.breed)  # Golden Retriever

dog2 = Dog("Max")
print(dog2.name)   # Max
print(dog2.breed)  # Mutt