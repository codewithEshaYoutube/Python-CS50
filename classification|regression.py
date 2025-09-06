def powerof4(number):
  count=0
  # apply bit calculations only 1 set bit
  if (number and(  number and (number-1))): # efficient
    while (number>1):
      number >>=1
      count+=1
    if (count %2==0):
      return True
    else:
      return False

numbers=int(input("Enter your number  "))
if powerof4(numbers):
  print(f"{numbers} This is power of 4")
else:
  print(f"{numbers} THis is not power of two")



def computerpower(x,y):
  # default total
  result=1
  while (y>0):
    # even y
    if (y%2==0):
      x=x*x
      y>>=1
    else:
      result=result*x
      y=y-1
  return result
x=int(input("Enter your value for x "))
y=int(input("Enter your value for y "))
print("Total: ",(computerpower(x,y)) )


