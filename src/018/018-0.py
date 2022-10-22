from turtle import Screen, Turtle

timmy = Turtle()

timmy.shape("turtle")
timmy.color("#0080ff")

for ea in range(4):
  timmy.forward(90)
  timmy.right(90)



screen = Screen()
screen.exitonclick()