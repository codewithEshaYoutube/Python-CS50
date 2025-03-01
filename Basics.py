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



"""
price of house is $1m
if buyer have good credit put down 10 percent if  not put down 20
print down payment
"""
good_credit=False
down_payment=int(input("down payment amount:"))
if good_credit is True:
        print("they need to put down 10%")
        print((down_payment)* float(0.1))
else:
        print("they need to put down 20%")
        print((down_payment) * float(0.2))
print (f" Down payment is : ${down_payment}")
"""
logical operators
Example 1: if employee has high income and credit than eligible for loan
"""
high_income = True
high_credit = False
is_adult = True
if high_income and high_credit:
    print("Employee is eligible")
elif not is_adult:
    print("Candidate is underage")

else:
    print('not eligible')
"""
and: both 
or: atleast one 
not: inverse

"""
#lists
names=["esh","sam","bob","mosh"]
names[0]="esha"
print(names[0:3])
print(names[-1])
print(names[-2])
print(names[0])
print(names)

#Challange to find largest num in list
nums=[1,5,6,7,8,11,14,78,3,1,33,27]
max=nums[0]

for num in nums:
        if num>max:
                max=num
print (max)
"""
2-dimentional list are matrices in pythin

matrix in maths=[ 567
                  577
                  555
                  ]
"""

matrix=[
        [5,6,7],
        [1,2,3],
        [7,4,6]

]
matrix[0][2]=12 #modification
#accesing
print(matrix[0][2])
print(matrix[2][1])
print(matrix[1][2])
for x in matrix:
        for y in x:
                print (y)


numbers=[1,4,55,6,78,43,66,77,6]
(numbers.append(22))
print (numbers)
(numbers.insert(2,7))
print (numbers)
(numbers.sort())
(numbers.reverse())
print (numbers)
#remove duplicates


numbers=[1,4,55,6,78,43,66,77,6]
unique=[]
for i in numbers:
        if i not in unique:
                unique.append(i)

print(unique)
#Tuple,Immutable denoted by ()
coordinates=(1,2,3)
'''
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

'''
x,y,z=coordinates #unpacking
print (y)
'''
Dictionaries: Key value pair, denoted by {}
Name:Esha
GMail:tariqeesha321@gmail.com
phonenumber:112434344
'''
customer={
        "name":"Esha",
        "age": 19,
        "class": "12th",
        "profession": "software Engineer",
        "is_verified":True
}
customer["age"]=20
customer["Smart_student"]= True
print(customer)
'''
Phone number is requested and give them nums in words
'''
nums=input("Enter your phone number  ")

Numbers_in_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output=""

output="".join(Numbers_in_mapping.get(ch,"!")for ch in nums)
print (output)
"""
emoji converter
"""

message=input("> ")
words=message.split(" ")
emoji_mapping={
        ":)" :"😊",
        ":(" :"😢",
        ";)" : "😉"
}
output=" "
output=" ".join(emoji_mapping.get(word,word)for word in words)
print (output)