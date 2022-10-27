from turtle import Screen

from snake import Snake
import time
from food import Food
from score import Scoreboard

WIN_HEIGHT = 688
WIN_WIDTH = 688
BORDER = int(WIN_HEIGHT / 2)
PADDING = 5 # border padding pixels

scr = Screen()
scr.setup(WIN_WIDTH, WIN_HEIGHT)
scr.bgcolor("black")
scr.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_on = True
while game_on:
    scr.update()  # update screen after segments move
    time.sleep(0.1)  # control the speed
    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect colision with wall
    location = snake.head
    if (
        location.xcor() > (BORDER - PADDING)
        or location.xcor() < ((BORDER * -1) + PADDING)
        or location.ycor() > (BORDER - PADDING)
        or location.ycor() < ((BORDER * -1) + PADDING)
    ):
        game_on = False
        scoreboard.game_over()
        # if hit boundary end game

    # Detect collision with tail
    for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
        game_on = False
        scoreboard.game_over()







scr.exitonclick()
