from turtle import Turtle, Screen

scr = Screen()

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.goto(0, 0)
    self.color("white")
    self.resizemode("user")
    self.speed(0)

  def move(self):
    current_pos = self.position()
    self.setx(current_pos[0]+1.5)
    self.sety(current_pos[1]+1)

