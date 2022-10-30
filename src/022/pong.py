from turtle import Screen as scr
from scoreboard import Scoreboard
import paddle
import ball
from scoreboard import Scoreboard

# Screen setup
WIN_HEIGHT = 600
WIN_WIDTH = 800
PADDING = 10 # border padding pixels
scr.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
scr.bgcolor("black")
scr.title("Pong")
scr.listen()

# Setup positive boundaries
TOP = int(WIN_HEIGHT / 2) - PADDING
RIGHT = int(WIN_WIDTH / 2) - PADDING

# Negative boundaries seem off by 5
BOTTOM = ((int(WIN_HEIGHT / 2)) * -1) + PADDING - 5
LEFT = ((int(WIN_WIDTH / 2)) * -1) + PADDING

score = Scoreboard(TOP, WIN_WIDTH, "white")

# Create paddles slightly inside padding
R_PADDLE_START = RIGHT - PADDING
L_PADDLE_START = LEFT + PADDING
L_paddle = paddle.Paddle(L_PADDLE_START)
R_paddle = paddle.Paddle(R_PADDLE_START)
scr.onkey(R_paddle.up, "Up" )
scr.onkey(R_paddle.down, "Down")
scr.onkey(L_paddle.up, "w" )
scr.onkey(L_paddle.down, "s")

# Create ball
ball = ball.Ball()

# Start game, loop til game_on = False
while True:
  ball.move()
  # detect ball hitting walls
  if (
      ball.ycor() > (TOP - PADDING)
      or ball.ycor() < (BOTTOM + PADDING)
  ):
    ball.y_bounce()
  # detect ball hitting paddles
  if (
      ball.distance(R_paddle) < 35
      and ball.ycor() < (TOP)
      or ball.distance(L_paddle) < 35
      and ball.ycor() < (TOP)
  ):
    ball.faster_ball() # make ball faster
    ball.x_bounce()
  # detect ball going past paddles
  if (
    ball.xcor() > RIGHT
    and ball.ycor() < TOP
    or ball.xcor() < LEFT
    and ball.ycor() > BOTTOM
  ):
    # When a player wins, overwrite the current score
    # in black color, then write again in white.
    if ball.xcor() > 0:
      score.erase_score()
      score.score1 +=1
      score.show_score()
    else:
      score.erase_score()
      score.score2 +=1
      score.show_score()
    ball.reset_position()




scr.exitonclick()