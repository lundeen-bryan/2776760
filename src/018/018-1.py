import turtle as tur

scr = tur.Screen()
tur.shape("turtle")
tur.color("#0080ff")

def dashed_line(space, x):
  for i in range(x):
    tur.pendown()
    tur.forward(space)
    tur.penup()
    tur.forward(space)

  tur.backward(space*x)
  tur.right(90)
  tur.forward(space)
  tur.left(90)

dashed_line(10, 10)
tur.hideturtle()
scr.exitonclick()

##===========================================================================================
## Date: .............. 2022-10-22
## Program: ........... 018-1.py
## Description: ....... make a dashed line with turtle
## Installs to: ....... src/018
## Compatibility: ..... Python3.10
## Contact Author: .... lundeen.bryan@gmail.com
## Copyright © ........ n/a 2022. All rights reserved.
##
## Notes:
##
##
##===========================================================================================
