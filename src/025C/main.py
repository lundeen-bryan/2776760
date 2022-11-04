import turtle
from turtle import Turtle
from turtle import Screen
import pandas as pd
from scoreboard import Scoreboard
import sys
sys.path.insert(0, "./src/") # imports file_control.py from this parent folder
import file_control as fc

# source data file
working_dir = "./src/025C/"
data_file = working_dir + "50_states.csv"
# get a data frame
data_frame = pd.read_csv(data_file)

# load turtle game
scr = Screen()
tur = Turtle()
img = Turtle()
scoreboard = Scoreboard()

# save screen and data parameters
WIN_HEIGHT = 600
WIN_WIDTH = 775
STATES_LIST = data_frame["state"].tolist()
STATES_COUNT = len(STATES_LIST)

# setup screen
scr.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
scr.title("U.S. States Game")
image = "./src/025C/blank_states_img.gif"
scr.addshape(image)
img.shape(image) # made image separate object from turtle that writes on screen

def write_state(x, y, state):
    tur.penup()
    tur.hideturtle()
    tur.goto(x, y)
    tur.write(state)
    tur.home()
    tur.showturtle()

# get coordinates where user clicks
def get_click_coord(x, y):
  print(x, y)

turtle.onscreenclick(get_click_coord)

# let user guess a state
title = "U.S. States Game"
prompt = "What's another state name?"
# convert ans to title case
current_guess = STATES_COUNT
states_remaining = []
for ea in STATES_LIST:
  states_remaining.append(ea)
while len(states_remaining) > 0:
  user_guess = scr.textinput(title=title, prompt=prompt).title()
  if user_guess == "Exit":
    break
  # check if guess is found in states list
  if user_guess in STATES_LIST:
    current_index = STATES_LIST.index(user_guess)
    print(data_frame[data_frame["state"] == user_guess])
    x_coord = data_frame[data_frame["state"] == user_guess].at[current_index, "x"]
    y_coord = data_frame[data_frame["state"] == user_guess].at[current_index, "y"]
    state_name = data_frame[data_frame["state"] == user_guess].at[current_index, "state"]
    write_state(x_coord, y_coord, state_name)
    scoreboard.increase_score()
    current_guess -= 1
    title = f"{current_guess} of {STATES_COUNT}"
    states_remaining.remove(user_guess)

learning_file = working_dir + "States to learn.csv"
fc.write_file(file_name=learning_file, new_text=states_remaining, overwrite=False)


turtle.mainloop()