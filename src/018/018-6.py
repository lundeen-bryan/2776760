import turtle as tur
import random as rand

tur.colormode(255)
scr = tur.Screen()

rgb_color_list = [
    (245, 243, 239),
    (247, 242, 245),
    (204, 165, 107),
    (239, 246, 241),
    (237, 240, 245),
    (155, 73, 46),
    (174, 154, 37),
    (51, 93, 124),
    (224, 201, 133),
    (139, 31, 20),
    (132, 163, 185),
    (201, 90, 69),
    (46, 123, 86),
    (13, 100, 73),
    (70, 48, 39),
    (99, 72, 74),
    (147, 179, 146),
    (235, 175, 164),
    (163, 141, 158),
    (55, 46, 50),
    (184, 206, 171),
    (18, 85, 90),
    (147, 18, 22),
    (41, 61, 74),
    (80, 146, 128),
    (187, 83, 87),
    (41, 66, 88),
    (108, 126, 151),
    (15, 72, 69),
    (175, 192, 213),
]

def draw_dots():
  for _ in range(columns): # 10 columns
    tur.fd(dot_spacing); tur.dot(dot_size, rgb_color_list[rand.randint(0, 29)]); tur.fd(dot_spacing)

def main():
  tur.speed(0) # fastest speed
  tur.penup() # lift pen so there's no line
  tur.hideturtle() # hideturtle so we only see dots
  x = starting_position
  y = x
  for _ in range(rows): # 10 rows
    tur.goto(x, y) # distance above starting position
    draw_dots()
    y += dot_size + dot_spacing # change starting position

# change these values to see different dot results
dot_size = 25
dot_spacing = 30
rows = 10
columns = 10
starting_position = -260

main()

scr.exitonclick()