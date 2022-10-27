from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT_NAME = "Arial"
FONT = 24
FONT_STYLE = "normal"
CURRENT_HEIGHT = Screen().window_height()
DISPLAY_SCORE = (CURRENT_HEIGHT/2) - FONT - 20 # half screen height - size of font - padding

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, DISPLAY_SCORE)
    self.hideturtle()
    self.update_scoreboard()

  def update_scoreboard(self):
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT_NAME, FONT, FONT_STYLE))

  def game_over(self):
    self.goto(0,0)
    self.write(f"GAME OVER.", align=ALIGNMENT, font=(FONT_NAME, FONT, FONT_STYLE))

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()
