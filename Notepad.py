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