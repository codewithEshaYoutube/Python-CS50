import turtle

s = turtle.Turtle()

Guess = int(input("What is 8 X 5?"))

if Guess == 8*5:
    s.write(str(Guess) + ' is correct!')
    s.penup()
    s.backward(10)
else:
    s.write('You said ' + str(Guess) + '. I got ' + str(8*5))
    s.penup()
    s.backward(10)
import turtle
s=turtle.Turtle()
s.shape("turtle")
s.penup()

age=int(input("What is your age "))
if age<=15 and age>=10:
  print("you are not eligible for voting")
  s.write("you are not eligible for voting")
  s.backward(20)
if age >16 and age<18:
  print("you are not eligible for voting")
  s.write("you are not eligible for voting")
  s.backward(20)
if age>=18:
  print("you are eligible for voting")
  s.write("you are  eligible for voting")
  s.backward(20)
else:
  print("age is not valid")
  s.write("age is not valid")
  s.backward(20)
