import turtle as tur
import random

scr = tur.Screen()

scr.setup(width=500, height=400)
bet = tur.textinput(title="Make Bet", prompt="Pick a turtle color ")
colors = ["red", "green", "orange", "blue", "yellow", "purple"]
turtles = []

x=-230
y=-125
a = 40 # distance between turtles
race_on = False

for ea in range(6):
  name = f"turtle_0{ea}"
  name = tur.Turtle(shape="turtle")
  name.penup()
  if ea > 0:
    y += a
  name.color(colors[ea])
  name.goto(x, y)
  turtles.append(name)

if bet:
  race_on = True

while race_on:
  for ea in turtles:
    if ea.xcor() > (250-30):
      race_on = False
      winner = ea.pencolor()
      if winner == bet:
        print(f"{winner} won!")
      else:
        print(f"{winner} won. Sorry, you lost.")
      break
    r_dist = random.randint(0, 10)
    ea.fd(r_dist)

scr.exitonclick()