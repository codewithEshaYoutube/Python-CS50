"""
Python Beginner Tutorial
This script covers the basics of Python programming with comments explaining each section.
"""

# Print function - Outputs text to the console
print("Hello, World!")

# Variables and Data Types
name = "Eesha"  # String
age = 21  # Integer
height = 5.6  # Float
is_student = True  # Boolean

# Displaying variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student Status:", is_student)

# Basic Arithmetic Operations
x = 10
y = 5
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)  # Remainder of division

# Lists - Ordered, mutable collection
fruits = ["Apple", "Banana", "Cherry"]
print("Fruits List:", fruits)
print("First Fruit:", fruits[0])  # Indexing starts at 0
fruits.append("Mango")  # Adding new element
print("Updated Fruits List:", fruits)

# Conditional Statements
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loops
# For Loop
for fruit in fruits:
    print("Fruit:", fruit)

# While Loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Functions
# Defining a function
def greet(name):
    """Function to greet a person"""
    return "Hello, " + name + "!"

# Calling a function
message = greet("Eesha")
print(message)

# Dictionaries - Key-Value pairs
student = {"name": "Eesha", "age": 21, "course": "Software Engineering"}
print("Student Info:", student)
print("Student's Course:", student["course"])

# Exception Handling
try:
    result = 10 / 0  # This will cause an error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# File Handling
with open("sample.txt", "w") as file:
    file.write("This is a sample file.")

print("Python Tutorial Completed!")
