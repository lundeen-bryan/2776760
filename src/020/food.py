from turtle import Turtle, Screen
import random

CURRENT_HEIGHT = Screen().window_height()
BORDER = int(CURRENT_HEIGHT/2) - 24

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.color("blue")
    self.speed("fastest")
    self.refresh()

  def refresh(self):
    random_x = random.randint((BORDER*-1), (BORDER))
    random_y = random.randint((BORDER*-1), (BORDER))
    self.goto(random_x, random_y)

