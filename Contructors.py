class Pointer:
    def __init__(self,x,y,e,r):
        self.x=x
        self.y=y
        self.e=e
        self.r=r
    def move(self):
        print("move in right")
    def play(self):
        print("playing with ball")
pointer1=Pointer(1,2,4,5)
print(pointer1.y)
print(pointer1.x)
print(pointer1.e)
print(pointer1.r)
#Exercise
class Person:
    def __init__(self,name,age):
        self.name=name
    def talk(self):
        print("I am talking to you")
person1=Person("esha",12)
person1.talk()
print (person1.name)
print (person1.name)

