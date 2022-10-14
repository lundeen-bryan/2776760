import os
from art import logo
from _clear_console import clear

def print_operators():
  """ Prints keys from operations dictinoary """
  symbol_list = []
  for ea in operations:
    symbol_list.append(ea)
  print(symbol_list)

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multily
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Calculator dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = int(input("What's the first number? "))
  print_operators()
  operation_pick = input("Pick an operation from the line above. ")
  num2 = int(input("What's the second number? "))
  calc_function = operations[operation_pick] # returns which func to call
  answer = calc_function(num1,num2) # sends numbers to func from above
  print(f"{num1} {operation_pick} {num2} = {answer}")

  clear_calculator = False
  while not clear_calculator:
    # calc another number to the answer
    print("Type C to clear type X to exit, or pick an operation from the line below.")
    print_operators()
    operation_pick = input(f"\n{answer} ")
    if operation_pick == "C" or operation_pick == "c":
      clear_calculator = True
      clear()
      print(logo)
      calculator() # restart function
    elif operation_pick == "X" or operation_pick == "x":
      clear_calculator = True # exit
    else:
      num3 = int(input("What's the next number? "))
      calc_function = operations[operation_pick]
      new_answer = calc_function(answer, num3)
      print(f"{answer} {operation_pick} {num3} = {new_answer}")
      answer = new_answer

clear()
print(logo)
calculator()
