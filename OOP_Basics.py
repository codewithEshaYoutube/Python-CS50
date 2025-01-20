from abc import ABC, abstractmethod

# ===========================
# Abstraction Example
# ===========================
# Abstraction is the concept of hiding the internal implementation details
# and exposing only the necessary parts of the object. In Python, this is
# typically done by using abstract classes.

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):
        # Abstract method - must be implemented by any subclass
        pass
    
    def eat(self):
        # Concrete method - shared by all animals
        print("Eating...")

# ===========================
# Encapsulation Example
# ===========================
# Encapsulation is the concept of bundling the data (attributes) and methods
# that operate on the data into a single unit or class. Additionally, we can
# restrict access to some of the object's components by making them private.
# This is typically done using 'private' or 'protected' attributes.

class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name  # public attribute
        self._breed = breed  # protected attribute (conventionally indicating restricted access)
        self.__age = 5  # private attribute (not directly accessible outside the class)
    
    def sound(self):  # Implementing the abstract method from Animal
        print(f"{self.name} barks!")
    
    # Encapsulation: Accessor method to access private attribute
    def get_age(self):
        return self.__age

    # Encapsulation: Mutator method to change private attribute
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

# ===========================
# Inheritance Example
# ===========================
# Inheritance allows a new class (child class) to inherit the properties and
# behaviors of an existing class (parent class). The child class can also
# override methods from the parent class to provide its own specific implementation.

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    def sound(self):  # Overriding the 'sound' method from Animal
        print(f"{self.name} meows!")

# ===========================
# Polymorphism Example
# ===========================
# Polymorphism allows objects of different types to be treated as objects
# of a common parent type. It allows the same method to behave differently
# depending on the object that calls it.

def animal_sound(animal):
    # Polymorphism in action: calling 'sound' method on different objects
    animal.sound()

# ===========================
# Testing Abstraction, Encapsulation, Inheritance, and Polymorphism
# ===========================
# Create instances of Dog and Cat
dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers")

# Abstraction: We can interact with 'sound' method without knowing implementation details
# Polymorphism in action: both objects (dog and cat) respond differently to the same method
animal_sound(dog)  # Rex barks!
animal_sound(cat)  # Whiskers meows!

# Encapsulation: Access private attribute via getter method
print(f"Dog's age: {dog.get_age()}")  # Dog's age: 5
dog.set_age(6)  # Changing the dog's age using setter
print(f"Updated dog age: {dog.get_age()}")  # Updated dog age: 6

# Inheritance: Cat inherits from Animal and implements 'sound' method
cat.sound()  # Whiskers meows!

