#whatevr w put in parent it child will get own methods and parent methods too
class Mammal:
    def hairs(self):

        print("have hairs")
class Dog(Mammal):
    def annoying(self):
        print("bark at you")
class Cat(Mammal):
    def meow(self):
        print("meow meow meow")
    def cute(self):
        print("cats are cuties")
dog1=Dog()
dog1.hairs()





