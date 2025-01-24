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
