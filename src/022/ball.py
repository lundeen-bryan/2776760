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
    self.x_ball_speed = 2.0
    self.y_ball_speed = 2.0

  def move(self):
    """set the ball speed higher for faster

    Args:
        ball_speed (float): floating num value
    """
    current_pos = self.position()
    self.setx(current_pos[0]+ self.x_ball_speed)
    self.sety(current_pos[1]+ self.y_ball_speed)

  def y_bounce(self):
    self.y_ball_speed *= -1

  def x_bounce(self):
    self.x_ball_speed *= -1
