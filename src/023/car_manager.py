from turtle import Turtle, Screen
import random

scr = Screen()

CURRENT_WIDTH = Screen().window_width()
CURRENT_HEIGHT = int((Screen().window_height())/2)
RIGHT_EDGE = int(CURRENT_WIDTH/2) - 48
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_CARS = 6

class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car_num = random.randrange(1, MAX_CARS)
        if random_car_num == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint((CURRENT_HEIGHT*-1), (CURRENT_HEIGHT))
            new_car.goto(RIGHT_EDGE, random_y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
