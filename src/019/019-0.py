import turtle as tur

scr = tur.Screen()

scr.listen()

def move_fwd():
  tur.fd(10)


scr.onkey(move_fwd, "space")
