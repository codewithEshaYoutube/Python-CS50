print("This is python") #String 
print(234)#Integer
print(3.789776)#Float
print("1655327")#String 
#comment
name = input("what's your name")
print("hello", name)

#variable is name 


patient_name = "john"
age = 20
New_patient = "True"

def print_patient_details():
    print(f"Patient Name :{patient_name }")
    print(f"Patient Age :{age }")
    print(f"New Patient :{New_patient}")

print_patient_details()

name = input("What is your Name")
print ("Hello Greetings"+ name)

# Age Calculation function by Esha Tariq
birth_year= input("what is your birth year")
age = 2025 - int(birth_year) # str to int conversion
print (age)
# float
first = input ("First:")
second = input ("Second:")
 
def print_sum_numbers():
  print(float(first) + float(second))

print_sum_numbers()
#Functions and methods

course= "This is  python beginner course by Esha Tariq"
print (course.upper())
print (course.lower())
print (course.casefold())
print (course.capitalize())
print (course.find("is"))
print (course.find("This"))
print (course.replace("by","with"))
print ("python"in course)

#Arthimetic Operators
print(4+3)#addition
print(4-3)#subtract
print(4*3)#multiply
print(4/3)#divide
print(4//3)#divide and round off ans
print(4%3) #remainder 
print(4**3) #power of number
x=99
# x= x-3
x -= 3 #augumented assignment operator
print(x)
"""
Comparison operators
> greater
< less than 
>= greater equal
<= less than equal
!= not equal
== equal
logical Operators
and : only true if both true
or : atleast one is true
not:inverse of value
"""
x= 4
print(x>3 and x<2)
print(x>3 or x<2)
print(not x<2)

# conditional statements
#while loop
i=1
while i<1_0:
  print (i*"↓")
  i=i+1
  
e=1
while e<1_0:
  print (e*"↑")
  e=e+1
#list and lists methods
numbers=[1,2,3,4,5,6]
numbers.append(7)    #add in order
numbers.insert(0,5)  #insert in between

numbers.remove(2)
numbers.clear
print (len(numbers))
print (1 in numbers)
print(numbers)
   # A compiler translates the entire source code into machine code at once,
# producing an executable file. This file can then be run independently.
# Example: C, C++, Java (Java compiles to bytecode which is interpreted by the JVM)

# A Python interpreter, on the other hand, translates the code line by line, 
# executing each instruction immediately.

# Let's write a simple Python code to demonstrate an interpreter's behavior.

# Sample Python code (this would be executed by an interpreter):
print("Hello, World!")  # This line will be executed immediately

# Now, let's compare the compiler and interpreter in comments.

# Compiler (e.g., C compiler):
# - Translates the entire code at once, producing an output file.
# - Errors are detected after the entire code is compiled.
# - Slower execution during the compilation phase but faster runtime.

# Interpreter (e.g., Python interpreter):
# - Translates the code line by line and executes it immediately.
# - Errors are detected during execution, at the point where they occur.
# - Slower execution overall, because code is being translated on the fly.

# For instance, in C, you would compile the code, and only after the compilation process,
# you would know if there are any errors.
# In Python, you can execute code line by line, and errors will be caught immediately.

# Example Python code execution (interpreter behavior):
def greet(name):
    print(f"Hello, {name}!")  # This will execute immediately when called

greet("Alice")  # Interpreter runs this line immediately and outputs: "Hello, Alice!"  

# In comparison, with a compiler (like C), you would write the code, compile it
# only see output after running the compiled executable.
# Imaginary Dog
print("O----")
print(" ||||")
print(45)