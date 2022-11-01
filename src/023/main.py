import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
WIN_HEIGHT = 600
WIN_WIDTH = 600
scr = Screen()
scr.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
scr.tracer(0)
scr.title("Turtle Game")
scr.listen()

player = Player()
car = CarManager()

scr.onkey(player.move, "Up" )

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()
    car.create_car()
    car.move_car()





scr.exitonclick()