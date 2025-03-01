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
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess the num:  "))
    guess_count+=1
    if guess == secret_num:
        print("You won")
        break
    if guess_count <= 2:
        print("You failed,Try again")

    else:
        print("You lost all chances")
#  while conditon
"""
1.Building car game:simulation of car game
2.if car istaretd earlier dont dtart again
3.if car i s stopped earlier don tstop again
"""
command = ""
started = False
while True:
    command=input("-->> ")
    if command == "start":
        if started:
            print("its already started")
        else:
            started=True
            print("car is started...")
    elif command == "stop":
        if  not started:
            print("its already stopped")
        else:
            started=False
            print("car is stopped...")
    elif command == "help":
        print("""
start: to start the car 
stop: to start car 
quit: to quit the game
        """)
    elif command=="quit":
        print("your game is ended...")
        break
    else:
       print("Sorry I don't Understand")

#for loop
"""
no. of iterations are known 
iterate over list tuple  strings
"""
for z in "python":
    print(f'letter is {z}') # dynamically implement variable

for i in range(25):
    print(f'number is {i}') # implement range function

#example list
prices=[10,20,30,40]
total=0

for price in prices:
    total+=price                                    #total=total+price(augmented operator)
print(f"Total of all prices are {total}")

"""
nested loops
"""
for i in range(3): # outer loop
    for j  in range (2): #inner loop
        print(f"({i},{j})")
#Challange
nums=[5,2,5,2,2]
for x in nums:
        print((x)*" x") # using built in funcitons

nums2=[5,2,5,2,5]
for i in nums2:
    output=""
    for j in range(i) :
        output+="x"
    print(output)
#lists
names=["esh","sam","bob","mosh"]
print(names)
#if_statements
"""
weather is hot outside
drinln plenty water
and enjoy andgthes
otherwisw its lovely weather

"""
is_hot=True
is_cold=False

if is_hot:
        print("its hot outside")
        print("drink plenty water")
elif is_cold:
        print("its cold outside")
        print("wear warm clothes")
else:
        print("its lovely weather")
print("enjoy your day")
