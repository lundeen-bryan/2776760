from menu import MENU
from menu import resources
from _clear_console import clear
from art import logo

KEYS = list(MENU.keys())
VALS = list(MENU.values())

def add_money(money):
  """Add money to the resources dict

  Args:
      money (float): value to add to the dictionary
  """
  resources["money"] += money

def decrease_supplies(supply_name, decrease_amount):
  # get current value
  current = resources.get(supply_name)
  current -= decrease_amount
  if current <= 0:
    current = 0
  resources[supply_name] = current
  if current == 0:
    print(f"We're sorry but we are currently out of {supply_name} 🙁.")
    return False
  else:
    return True

# Show user a menu with prices
def show_menu():
  """Show a menu with prices to the user
  """
  num = 1
  for ea in KEYS:
    price_tag = "${:,.2f}".format(MENU[KEYS[num - 1]]["cost"])
    print(f"{num}) {ea} | cost: {price_tag}")
    num += 1

# Store drink supplies for items on menu

# When user enters coins, display total due
def collect_money(total_price):
  """Collect money from user, ensure it can purchas the drink

  Args:
      total_price (float): total cost of the drink
  """
  # iterate through this dictionary asking for
  # incremental values until drink is paid for
  coins = {
    "quarters": .25,
    "dimes": .1,
    "nickles": .05,
    "pennies": .01
  }
  money = 0.0
  due = total_price
  while due > 0:
    for coin_name in coins: # Coin names are Quarters, dimes, etc.
      print(f"How many {coin_name}?")
      user_drops = input("> ").strip()
      coin_value = coins.get(coin_name)
      money = int(user_drops) * coin_value
      # ^--multiply coin value by # of coins dropped in the machine
      due -= money # anymore money needed to pay?
      display_due = "${:,.2f}".format(due)
      if due <=0:
        break
      print(f"Total Due is: {display_due}")
  # Give user their change back
  if due < 0:
    change = due * (-1)
    print("Here is " + "${:,.2f}".format(change) + " in change.")
  add_money(total_price)

def check_supplies():
  for key, value in resources.items():
    if value <= 1:
      print(f"I'm sorry we're currently out of {key}")
      exit(0)

def main():
  check_supplies()
  print("Please pick a drink from below by entering a number between 1-3.")
  print("Type (O)ff to turn off the machine.")
  print("Type (R)eport for a report of supplies.")
  show_menu()
  drink = input("> ").strip()
  if drink == "O":
    print("Goodbye")
    exit(0)
  elif drink == "R":
    for key, value in resources.items():
      print(key, ": ", value)
    drink = input("> ").strip() # ask for new input
  price = "${:,.2f}".format(MENU[KEYS[int(drink) - 1]]["cost"])
  user_chose = str(KEYS[int(drink)-1])
  print(f"You chose {user_chose}")
  in_stock = True
  if str(user_chose) == "espresso":
    in_stock = decrease_supplies("water", 50)
    in_stock = decrease_supplies("coffee", 18)
  elif str(user_chose) == "latte":
    in_stock = decrease_supplies("water", 200)
    in_stock = decrease_supplies("coffee", 24)
    in_stock = decrease_supplies("milk", 150)
  elif str(user_chose) == "cappuccino":
    in_stock = decrease_supplies("water", 250)
    in_stock = decrease_supplies("coffee", 24)
    in_stock = decrease_supplies("milk", 100)
  if in_stock == False:
    return # exit main
  print(f"Please insert {price}")
  collect_money(MENU[KEYS[int(drink) - 1]]["cost"])
  print(f"Here is your {user_chose} ☕. Enjoy!\n")
  return

clear()
print("\nWelcome to BryBucks Coffee may I take your order?\n")
main()
while input("Would you like to place another order? (Y)es/(N)o > ").upper() == "Y":
  clear()
  # if they want to play call main again
  main()
  print("Have a nice day. Thank you. Come again. 😊")