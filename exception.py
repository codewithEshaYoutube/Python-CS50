#this repo is all about how we gonna handle exceptions
try:
    age=int(input("age:"))
    print(age)
except ValueError:
    print("invalid value")
