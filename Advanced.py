# Advanced Python Concepts Example

# 1. Decorators
# A decorator is a function that modifies the behavior of another function. 
# Here, we'll create a simple decorator that logs function calls.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)  # Call the decorated function
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

# Applying the decorator
@log_decorator
def add(a, b):
    return a + b

add(3, 5)  # Logs the function call and result

# 2. Context Managers
# Context managers allow us to manage resources such as file handling in an elegant and safe way.

class MyContextManager:
    def __enter__(self):
        print("Entering the context manager")
        return "Resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context manager")
        if exc_type:
            print(f"Exception {exc_type} occurred: {exc_val}")
        return True  # Suppress exceptions

# Using the context manager
with MyContextManager() as resource:
    print(f"Inside the context manager, using {resource}")
    # Uncomment the next line to see exception handling in action:
    # raise ValueError("Something went wrong!")

# 3. Lambda Functions
# Lambda functions are small anonymous functions defined using the 'lambda' keyword.

# Here's a simple lambda function that adds two numbers:
add_lambda = lambda x, y: x + y
print(f"Lambda function result: {add_lambda(10, 5)}")

# 4. List Comprehension with Conditionals
# List comprehensions can include conditionals to filter or modify data in a more concise way.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

# 5. Generators
# A generator is a function that yields a sequence of values instead of returning them all at once.
# This can help save memory when working with large datasets.

def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count  # This 'yields' the value to the caller
        count += 1

# Using the generator
counter = count_up_to(5)
for num in counter:
    print(f"Generated number: {num}")

# 6. Destructuring (Unpacking)
# Python allows destructuring or unpacking of iterables into variables, making it easier to extract values.

person = ("John", 30, "Engineer")
name, age, occupation = person
print(f"Name: {name}, Age: {age}, Occupation: {occupation}")

# 7. Advanced Data Structures (Using defaultdict)
# defaultdict is a subclass of the built-in dict that provides a default value for nonexistent keys.

from collections import defaultdict

# Creating a defaultdict that returns '0' if a key does not exist
frequency = defaultdict(int)

# Counting occurrences of elements
for char in "hello world":
    frequency[char] += 1

print("Character frequencies:", dict(frequency))

# 8. Metaclasses
# Metaclasses are classes that define the behavior of other classes. It’s an advanced topic for controlling class creation.

class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'Meta'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(f"MyClass created by: {obj.created_by}")

# 9. Type Annotations
# Type annotations help provide better code clarity and allow static type checkers to catch potential issues.

def greet(name: str) -> str:
    return f"Hello, {name}!"

# The function expects a string argument, and will return a string
print(greet("Alice"))

# 10. Asyncio for Asynchronous Programming
# Asyncio is a library used to write asynchronous code that can improve performance in I/O-bound tasks.

import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulating I/O operation
    return "Data fetched"

async def main():
    data = await fetch_data()
    print(data)

# Running asynchronous code
asyncio.run(main())

# End of advanced Python examples

