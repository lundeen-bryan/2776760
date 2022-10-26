from turtle import Screen
from snake import Snake
import time

DISTANCE = 20

scr = Screen()
scr.setup(width=688, height=688)
scr.bgcolor("black")
scr.title("My Snake Game")

snake = Snake()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_on = True
while game_on:
  scr.update() # update screen after segments move
  time.sleep(0.1) # control the speed
  snake.move_snake()


scr.exitonclick()