from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#008000")
        self.penup()
        self.starting_line()
        self.seth(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def crossed_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def starting_line(self):
        self.goto(STARTING_POSITION)