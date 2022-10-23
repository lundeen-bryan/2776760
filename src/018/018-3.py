# See end of file for information
import turtle as tur
import random as ran

tur.colormode(255)
scr = tur.Screen()
tur.hideturtle()
head_list = [0, 90, 180, 270]
go_turtle = True
scr.listen()

def random_color():
  """returns a random color (RGB)

  Returns:
      tuple: an RGB color
  """
  color_list = []
  for _ in range(3):
    color_list.append(ran.randint(0, 255))
  new_color = tuple(color_list)
  return new_color

def stop_turtle():
  """pauses the drawing but doesn't exit screen
  """
  global go_turtle
  go_turtle = False

def setup_turtle():
  """setup turtle speed, and instructions
  """
  tur.speed(10) # max speed
  tur.width("10")
  tur.penup()
  tur.goto(0, 315)
  tur.write("INSTRUCTIONS:", True, align="left", font=("Arial", 12, "bold"))
  tur.goto(0, 295)
  tur.write("1. Press s to stop drawing.", True, align="left", font=("Arial", 12, "normal"))
  tur.goto(0, 275)
  tur.write("2. Click screen to exit.", True, align="left", font=("Arial", 12, "normal"))
  tur.home()
  tur.pendown()
  tur.speed(8) # fast but not too fast

def main():
  """draw random design until s key is pressed
  """
  global go_turtle
  while go_turtle:
    scr.onkey(stop_turtle, "s")
    head = ran.choice(head_list)
    col = random_color()
    tur.pencolor(col)
    tur.seth(head)
    tur.forward(25)

setup_turtle()
main()

scr.exitonclick()

##===========================================================================================
## Date: .............. 2022-10-23
## Program: ........... 018-3.py
## Description: ....... Draws random paths in random colors in python turtle
## Installs to: ....... src/018
## Compatibility: ..... Python3+
## Contact Author: .... github.com/lundeen-bryan
## Copyright © ........ 2022. All rights reserved. see repo.
##
## Notes:
## Part of Angela Yu's 100 Days of Code Python course. Day 18.
## I added a pause event with the key "s" and instructions at the top of the turtle screen.
##
##===========================================================================================
