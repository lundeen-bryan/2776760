from turtle import Screen
import paddle
import ball

scr = Screen()

WIN_HEIGHT = 600
WIN_WIDTH = 800
CURRENT_HEIGHT = scr.window_height()
R_PADDLE_START = int(scr.window_width()/2) - 24
L_PADDLE_START = (int(scr.window_width()/2) - 24) *-1
BORDER = int(WIN_HEIGHT / 2)
PADDING = 10 # border padding pixels

scr.setup(WIN_WIDTH, WIN_HEIGHT)
scr.bgcolor("black")
scr.title("Pong")
scr.listen()

L_paddle = paddle.Paddle(L_PADDLE_START)
R_paddle = paddle.Paddle(R_PADDLE_START)

scr.onkey(R_paddle.up, "Up" )
scr.onkey(R_paddle.down, "Down")
scr.onkey(L_paddle.up, "w" )
scr.onkey(L_paddle.down, "s")

ball = ball.Ball()

game_on = True
while game_on:
  ball.move()
  if (
      ball.ycor() > (BORDER - PADDING)
      or ball.ycor() < ((BORDER * -1) + PADDING)
  ):
    ball.y_bounce()
  if (
      ball.distance(R_paddle) < 35
      and ball.xcor() > (BORDER - PADDING)
      or ball.distance(L_paddle) < 35
      and ball.xcor() < ((BORDER * -1) + PADDING)
  ):
    ball.x_bounce()





scr.exitonclick()