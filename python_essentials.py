

# 1. VARIABLES AND DATA TYPES
x = 10  # Integer
pi = 3.14  # Float
name = "Python"  # String
is_fun = True  # Boolean

# 2. PRINT FUNCTION
print("Hello, World!")  # Outputs text to the console

# 3. USER INPUT
user_name = input("Enter your name: ")  # Takes input from user
print("Hello,", user_name)

# 4. CONDITIONALS (IF-ELSE)
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 5. LOOPS
# FOR LOOP
for i in range(5):  # Loops 5 times (0 to 4)
    print("Iteration:", i)

# WHILE LOOP
count = 0
while count < 5:
    print("Count is", count)
    count += 1  # Increment count


# 6. FUNCTIONS
def greet(name):
    """Function that greets the user."""
    return "Hello, " + name


print(greet("Alice"))

# 7. LISTS
fruits = ["apple", "banana", "cherry"]  # List of strings
print(fruits[0])  # Accessing first element
fruits.append("orange")  # Adding an element

# 8. DICTIONARIES
student = {"name": "John", "age": 20, "grade": "A"}  # Dictionary
print(student["name"])  # Accessing value

# 9. EXCEPTION HANDLING
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")


# 10. CLASSES AND OBJECTS
class Person:
    """Class representing a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


person1 = Person("Alice", 25)
print(person1.introduce())

# 11. FILE HANDLING
with open("sample.txt", "w") as file:
    file.write("Hello, file!")  # Writing to a file

with open("sample.txt", "r") as file:
    content = file.read()  # Reading from a file
    print(content)

# 12. IMPORTING MODULES
import math

print(math.sqrt(16))  # Using sqrt function from math module

# 13. LIST COMPREHENSION
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# 14. LAMBDA FUNCTIONS
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8
"""
====================================
# Best Tools for Python Project Visualization in PyCharm & VS Code
====================================
# PyCharm:
# - Built-in Scientific Mode for interactive data visualization.
# - Supports Jupyter Notebooks for better visualization.
# - Integration with Matplotlib, Seaborn, and Plotly for graphs.
# - Debugger with inline variable visualization.

# VS Code:
# - Jupyter Notebook extension for interactive coding.
# - Python Interactive Window for real-time visualization.
# - Built-in support for Matplotlib, Seaborn, and Pandas.
# - Live Share for collaborative visualization.
         
"""

