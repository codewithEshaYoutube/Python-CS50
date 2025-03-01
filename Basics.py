 # This is a basic Python program

# 1. Print statement
print("Hello, World!")

# 2. Variables and Data Types
name = "Alice"       # String
age = 25             # Integer
height = 5.5         # Float

# 3. Using variables
print("Name:", name)
print("Age:", age)
print("Height:", height)

# 4. Basic arithmetic
a = 10
b = 3

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# 5. Conditional Statements
if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

# 6. A simple function
def greet(person):
    return f"Hello, {person}!"

# Using the function
greeting = greet(name)
print(greeting)

# 7. A loop (for loop)
for i in range(5):
    print("Counting:", i)

# 8. List and loop through it
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#while loop
x=0
while x <=40:
    print (x)
    x+=4
print('done')
e=1
while e <=10:
    print("*"*e)
    e+=1
print('done')

#guess game using while loop
secret_num=7
guess_count=0
guess_limit=4
while guess_count<guess_limit:
    guess=int(input("Guess the num:  "))
    guess_count+=1
    if guess == secret_num:
        print("You won")
        break
    else:
        print("You failed,Try again")



