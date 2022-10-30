from turtle import Turtle, Screen

scr = Screen()

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.goto(0, 0)
    self.color("white")
    self.resizemode("auto")
    self.default_ball_speed = 2.5
    self.x_ball_speed = self.default_ball_speed # Horizontal speed
    self.y_ball_speed = self.default_ball_speed # Vertical speed
    self.difficulty_multiplier = 1 # makes ball faster & sharper angle

  def move(self):
    """set the ball speed higher for faster

    Args:
        ball_speed (float): floating num value
    """
    current_pos = self.position()
    self.setx(current_pos[0]+ self.x_ball_speed * self.difficulty_multiplier)
    self.sety(current_pos[1]+ self.y_ball_speed * self.difficulty_multiplier)

  def y_bounce(self):
    self.y_ball_speed *= -1

  def x_bounce(self):
    self.x_ball_speed *= -1

  def faster_ball(self):
    self.difficulty_multiplier += 0.03

  def reset_position(self):
    # Hide then show object
    self.hideturtle()
    self.goto(0, 0)
    self.showturtle()
    self.difficulty_multiplier = 1
