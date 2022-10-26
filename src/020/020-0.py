import turtle as tur
import time

scr = tur.Screen()
scr.setup(width=688, height=688)
scr.bgcolor("black")
scr.title("My Snake Game")

segments = []
snake_xy = [0,0]

x=0
y=0
a = 20 # distance between turtles (also size)
dist = 20

scr.tracer(0, 25)

for ea in range(3):
  name = f"seg_{ea}"
  name = tur.Turtle(shape="square")
  name.penup()
  name.color("white")
  if ea > 0:
    snake_xy[0] += a
  name.goto(snake_xy[0], snake_xy[1])
  segments.append(name)


game_on = True
count = 0 # temporarily use counter to stop loop
while game_on:
  scr.update()
  for seg in segments:
    if count > 30:
      game_on = False
      break
    for seg_num in range(len(segments) - 1, 0, -1):
      segments[seg_num].goto()
    seg.forward(dist)
    count += 1
    time.sleep(0.05)

scr.exitonclick()