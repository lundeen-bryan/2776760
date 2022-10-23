import turtle as tur

scr = tur.Screen()
tur.shape("classic")
tur.color("#0080ff")
color_list = ["", "", "", "#00ff40", "#ff8040", "#ff8080", "#ff0080", "#804000", "#800080", "#408080", "#80ffff"]

def draw_shape(sides, degrees, color):
  tur.pencolor(color)
  for i in range(sides):
    if i == sides - 1:
      tur.penup()
    tur.right(degrees)
    tur.forward(100)
    tur.pendown()

def start_pos(show_pen):
  if show_pen == False:
    tur.penup()
    tur.goto(0,300)
    tur.pencolor("#00ff40")
    tur.pendown()
    tur.forward(100)
  else:
    tur.penup()
    tur.goto(100, 300)
    tur.pendown()

def degrees(sides):
  return float(360/int(sides))

def main():
  start_pos(True)
  x = 3
  while x <= 10:
    draw_shape(x, degrees(x), color_list[x])
    x += 1
  start_pos(False)

main()

scr.exitonclick()