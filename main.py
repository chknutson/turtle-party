# Turtle Project
# by Chris Knutson
# 06.22.2023

import turtle

turtle.color("turquoise")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
# helper function 
# makes input, then multiplies it to make a negative and runs that through the back funtion
def move(len):
  back(-1 * len)

def right(len):
  left(-1 * len)

# movement function
def left(len):
  turtle.penup()
  turtle.left(90)
  turtle.pendown()

# drawn function on screen
def polygon(sides, size):
  for i in range(sides):
    turtle.forward(size)
    turtle.left(360 / sides)

def spiral(len, angle):
  for i in range(len , 5, -5):
    turtle.forward(i)
    turtle.left(angle)
  
spiral(50,33)
move(95)
left(50)
turtle.color("blue")
spiral(65, 45)
move(80)
left(50)
turtle.color("red")
spiral(30, 90)
move(75)
turtle.color("green")
polygon(5, 50)
