

# 1. VARIABLES AND DATA TYPES
# Problem: Swap two numbers without using a third variable
x, y = 5, 10
x, y = y, x
print(x, y)  # Expected Output: 10 5

# 2. PRINT FUNCTION
# Problem: Print a pattern using a single print statement
print("*\n**\n***\n****")

# 3. USER INPUT
# Problem: Take user input and print its type
user_input = input("Enter something: ")
print("You entered:", user_input, "Type:", type(user_input))

# 4. CONDITIONALS (IF-ELSE)
# Problem: Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 5. LOOPS
# Problem: Print numbers from 1 to 10 using a loop
for i in range(1, 11):
    print(i, end=" ")  # Output: 1 2 3 4 5 6 7 8 9 10
print()

# 6. FUNCTIONS
# Problem: Create a function to find the factorial of a number
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))  # Expected Output: 120

# 7. LISTS
# Problem: Find the largest number in a list
numbers = [3, 7, 2, 9, 5]
print(max(numbers))  # Output: 9

# 8. DICTIONARIES
# Problem: Count the occurrences of words in a sentence
sentence = "apple banana apple orange banana apple"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

# 9. EXCEPTION HANDLING
# Problem: Handle division by zero error
try:
    result = 10 / int(input("Enter a number: "))
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 10. CLASSES AND OBJECTS
# Problem: Create a class representing a Car with attributes and a method
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def details(self):
        return f"Car: {self.brand} {self.model}"
car1 = Car("Toyota", "Corolla")
print(car1.details())

# 11. FILE HANDLING
# Problem: Write and read a file
with open("test.txt", "w") as file:
    file.write("Hello, File Handling!")
with open("test.txt", "r") as file:
    print(file.read())

# 12. IMPORTING MODULES
# Problem: Generate a random number between 1 and 100
import random
print(random.randint(1, 100))

# 13. LIST COMPREHENSION
# Problem: Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, ..., 100]

# 14. LAMBDA FUNCTIONS
# Problem: Sort a list of tuples by the second value
data = [("apple", 3), ("banana", 1), ("orange", 2)]
data.sort(key=lambda x: x[1])
print(data)