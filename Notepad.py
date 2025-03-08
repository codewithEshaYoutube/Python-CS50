#Exception Handling
try:
    user=int(input("what is your age "))
    print(user)
except ValueError:
    print("Invalid Value,Value should be a Number")