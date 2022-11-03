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
cars = CarManager()
scoreboard = Scoreboard()

scr.onkey(player.move, "Up" )

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()

    cars.create_car()
    cars.move_car()

    #Detect collision with car
    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect successful crossing
    if player.crossed_finish_line():
        player.starting_line()
        cars.level_up()
        scoreboard.increase_level()







scr.exitonclick()