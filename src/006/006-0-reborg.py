def turn_right():
    for ea in range(3):
        turn_left()

def jump():
  turn_left()
  while not right_is_clear():
    move()
  turn_right()
  move()
  turn_right()
  while front_is_clear():
    move()
  turn_left()

while not at_goal():
  if wall_in_front():
    jump()
  else:
    move()

""" maze exercise """
def turn_right():
    for ea in range(3):
        turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else():
        turn_left()