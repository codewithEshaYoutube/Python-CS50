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
        self.age = age
    def talk(self):
        print("I am talking to you")
person1=Person("esha",12)
person1.talk()
print (person1.name)

class fruit:
  # contructors
  def __init__(self,name,color):
    self.name=name
    self.color=color
  # methods
  def intro(self):
    print("Hello I am ",self.name)
  # object creation
apple=fruit("apple","red")
apple.intro()
#enumerate method
l1=["orange","banana","grapes"]
obj1=enumerate(l1)
print(list(enumerate(l1)))



print (person1.age)

class NumberPair:
  def __init__(self,a,b):
    self.a=a
    self.b=b

  def addNum(self):
    return self.a+self.b
  def multiplyNum(self):
    return self.a*self.b
# objects making
pair1=NumberPair(3,6)
pair2=NumberPair(13,5)

print(" pair 1 -->  Multiply :",pair1.multiplyNum(), "Add:",pair1.addNum())
print(" pair 2 -->  Multiply :",pair2.multiplyNum(), "Add:",pair2.addNum())

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


