##===========================================================================================
## Date: .............. 2022-11-06
## Program: ........... playground.py
## Website: ........... n/a
## Description: ....... asks user to enter numbers and shows sum
## Installs to: ....... src/027
## Compatibility: ..... Python3
## Contact Author: .... lundeen-bryan
## Copyright © ........ n/a 2022. All rights reserved.
## Called by: ......... other_subs
## Called to: ......... other_subs
## Arguments: ......... numbers entered by user unlimited
##
## Notes:
## Project part of Angela Yu's python course day 27 talking about using tkinter.
## I attempted to improve the UI in this function.
## Main func asks user to enter numbers and if they do not enter anything then it breaks
## the while loop and sends a list to the add function.
## Have to convert args to a list bcuz args may contain characters that can't be converted.
##
##===========================================================================================
import os

def clear():
  os.system("clear")

def add(*args):
  result = 0
  add_nums = ""
  count = 1
  numbers = [item for lst in args for item in lst]
  for ea in numbers:
    result += int(ea)
    if count < len(numbers):
      add_nums += str(ea + " + ")
    else:
      add_nums += ea
    count +=1
  return f"{add_nums} = {result}"

def main():
  inputing = True
  numbers = []
  while inputing:
    print("Enter a number to add, or press [ENTER] to calculate")
    user_input = input("> ").strip()
    if user_input != "":
      if user_input.isdigit():
        numbers.append(user_input)
      else:
        print("You can only add numbers")
    elif user_input == "":
      if len(numbers) < 2:
        print("You must enter at least two numbers.")
      elif len(numbers) >= 2:
        inputing = False
  print(add(numbers))

clear()
main()