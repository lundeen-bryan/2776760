from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIN_HEIGHT = 688
WIN_WIDTH = 688
V_BORDER = int(WIN_HEIGHT / 2)
H_BORDER = int(WIN_WIDTH / 2)
PADDING = 5 # border padding pixels

screen = Screen()
screen.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    location = snake.head
    if (
        location.xcor() > (V_BORDER - PADDING)
        or location.xcor() < ((V_BORDER * -1) + PADDING)
        or location.ycor() > (H_BORDER - PADDING)
        or location.ycor() < ((H_BORDER * -1) + PADDING)
    ):
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
        game_on = False
        scoreboard.reset()





screen.exitonclick()
