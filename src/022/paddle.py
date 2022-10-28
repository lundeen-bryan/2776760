from turtle import Turtle

WIDTH = float(20/25) # =0.8
HEIGHT = float(100/20) # =5

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.penup()
    self.goto(position, 0)
    self.color("white")
    self.resizemode("user")
    self.shapesize(HEIGHT, WIDTH, 0) #reverse h/w because the line is vertical
    self.speed(0)

  def up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

  def down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
