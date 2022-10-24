import turtle as tur

scr = tur.Screen()

scr.listen()

def w(): # Forwards
  tur.fd(10)

def s(): # Backwards
  tur.bk(10)

def a(): # Counter-Clockwise
  tur.circle(50, 45)

def d(): # Clockwise
  tur.circle(-50, 45)

def c(): # Erase
  tur.reset()

scr.onkeypress(w, "w")
scr.onkeypress(s, "s")
scr.onkeypress(a, "a")
scr.onkeypress(d, "d")
scr.onkeypress(c, "c")

tur.exitonclick()