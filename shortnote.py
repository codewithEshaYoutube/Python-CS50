# 1. Variables and Data Types
# Variables store values, and Python automatically determines their type.
x = 10          # Integer
y = "Hello!"    # String
z = 3.14        # Float
print(x, y, z)  # Output: 10 Hello! 3.14

# 2. Control Flow (If-Else Statements)

if x > 5:
    print("x is greater than 5")  # This will run because x is 10.
else:
    print("x is less than or equal to 5")

# 3. Loops (For and While)
# For loop - iterates over a range or a list.
print("For loop example:")
for i in range(1, 6):  # range(1, 6) gives numbers 1 through 5
    print(i)  # Output: 1, 2, 3, 4, 5

# While loop - runs as long as a condition is true.
print("While loop example:")
count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1  # Increases count by 1 each iteration

# 4. Functions
# Functions are blocks of reusable code that can take inputs and return outputs.
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# 5. List Comprehension
# A compact way to create lists in one line.
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]  # Squares each number in the list
print(squares)  # Output: [1, 4, 9, 16, 25]

# 6. Dictionaries
# A dictionary stores data as key-value pairs.
person = {
    "name": "John",
    "age": 25,
    "location": "New York"
}
print(person["name"])  # Output: John

# 7. Error Handling (Try-Except)
# Handling errors gracefully using try-except blocks.
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")  # This will be printed.

# 8. Classes and Objects
# Classes allow you to model real-world objects.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"

my_car = Car("Tesla", "Model S")
print(my_car.display_info())  # Output: Tesla Model S

# 9. Lambda Functions
# A lambda function is a small anonymous function.
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

# 10. File Handling
# Python allows reading and writing to files.
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is Python!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, this is Python!
