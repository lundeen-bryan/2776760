# See end of file for information
from cgitb import reset
import turtle as tur
import random as ran

scr = tur.Screen()
tur.colormode(255)
go_turtle = True
scr.listen()

def stop_turtle():
  """pauses the drawing but doesn't exit screen
  """
  global go_turtle
  go_turtle = False

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

def draw_circle():
  """draws a circle and sets heading 5 degrees off
  """
  tur.circle(70)
  tur.pencolor(random_color())
  head = tur.heading()
  tur.seth(head + 5)

def setup_turtle():
  """setup turtle speed, and instructions
  """
  user_speed = tur.textinput("Drawing speed: ", "Enter 0 for fastest, 1 for slowest, up to 10 to go faster.")
  tur.speed(int(user_speed))
  tur.penup()
  tur.goto(0, 315)
  tur.write("INSTRUCTIONS:", True, align="left", font=("Arial", 12, "bold"))
  tur.goto(0, 295)
  tur.write("1. Press s to stop drawing.", True, align="left", font=("Arial", 12, "normal"))
  tur.goto(0, 275)
  tur.write("2. Click screen to exit.", True, align="left", font=("Arial", 12, "normal"))
  tur.home()
  tur.pendown()

def main():
  reset()
  turtle_start = tur.heading()
  global go_turtle
  while go_turtle:
    scr.onkey(stop_turtle, "s")
    draw_circle()
    turtle_end = tur.heading()
    if turtle_end == turtle_start:
      go_turtle = False

setup_turtle()
main()

scr.exitonclick()
##===========================================================================================
## Date: .............. 2022-10-23
## Program: ........... 018-4.py
## Website: ........... weburl
## Description: ....... Draw concentric circles w/random colors
## Installs to: ....... src/018
## Compatibility: ..... Python3+
## Contact Author: .... github.com/lundeen-bryan
## Copyright © ........ 2022. All rights reserved.
##
## Notes:
## Part of Angela Yu's 100 Days of Code Python course. Day 18.
## I added a pause event with the key "s" and instructions at the top of the turtle screen.
## Also an input for the user to choose the speed of the drawing.
##
##===========================================================================================


