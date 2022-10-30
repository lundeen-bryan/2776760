from turtle import Turtle


class Scoreboard(Turtle):
  """initializes the scoreboard

  Args:
      Turtle (class): _description_
      top_border (int): the length from center of window to the top of the window
      win_width (int): the length of the window
      player (int): player 1 or 2
      font_color (string): the color to use for the font
  """
  def __init__(self, top_border, win_width, font_color):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.score_font = 60
    self.score1 = 0
    self.score2 = 0
    self.win_width = win_width
    self.font_color = font_color
    self.top_border = top_border
    win_divided = (self.win_width/20) # div by 20% so scores are 20% from center
    self.player1_position = (win_divided * - 1 - self.score_font, (self.top_border - 10 - self.score_font)) # Left always off
    self.player2_position = (win_divided, (self.top_border - 10 - self.score_font))
    self.font_style = "normal"
    self.show_score()

  def erase_score(self):
    fill_color = "black"
    self.fillcolor(fill_color)
    self.begin_fill()
    #self.color(fill_color)
    self.goto(self.player1_position)
    self.pencolor(fill_color)
    self.pendown()
    for _ in range(2):
      self.fd(200)
      self.left(90)
      self.fd(100)
      self.left(90)
    self.end_fill()
    self.penup()
    self.color("white")

  def show_score(self):
    #self.change_color() # 1st loop change from white to black, 2nd from black to white
    # create player 1 score
    self.goto(self.player1_position)
    self.write(self.score1, align="left", font=("Courier", self.score_font, self.font_style))
    # create player 2 score
    self.goto(self.player2_position)
    self.write(self.score2, align="left", font=("Courier", self.score_font, self.font_style))