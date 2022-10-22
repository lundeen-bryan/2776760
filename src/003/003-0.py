from ast import If

from numpy import minimum


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

minimum_height = 120

if height >= minimum_height:
  print(f"{height} is tall enough. You can ride the roller coaster!")
else:
  print(f"{height} is not tall enough. You can't ride the rollder coaster until you are {minimum_height} first.")
