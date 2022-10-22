import time
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from _clear_console import clear

brybucks_coffee_menu = Menu()
coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()

# Get the cost of a drink
def return_cost(drink):
  drink_menu_item = brybucks_coffee_menu.find_drink(drink)
  drink_cost = drink_menu_item.cost
  return drink_cost

# Check supply level
def check_supply(drink):
  drink_menu_item = brybucks_coffee_menu.find_drink(drink)
  supply_sufficient = coffee_machine.is_resource_sufficient(drink_menu_item)
  if supply_sufficient == False:
    print(f"We're sorry we don't have your {drink} available at this time.")
  return supply_sufficient

# Show user menu
def show_menu():
  menu = []
  menu = brybucks_coffee_menu.get_items()
  drink_names_list = menu.split("/")
  x = 0
  for ea in range(len(drink_names_list) - 1):
    x += 1
    drink_cost = "${:,.2f}".format(return_cost(drink_names_list[ea]))
    print(f"{x}) {drink_names_list[ea]} - {drink_cost}")
  print("\nPlease pick a drink from the list above by entering a number between 1-3.")
#  print("Type (O) to turn off the machine.")
# Off is a secret command
  print("Type (R) for a report of supplies.")

# Process coins
def count_coins_entered(total_price):
  coins = cash_register.COIN_VALUES
  money = 0.0
  due = total_price
  total_paid = 0
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
        total_paid = total_price
        break
      print(f"Total Due is: {display_due}")
  # Add money to register & give user their change back
  if due < 0:
    change = due * (-1)
    total_paid = total_price + change
  cash_register.make_payment(total_price, total_paid)

def end():
  print("Have a nice day. Thank you. Come again. 😊")

def make_more():
  while input("Would you like to place another order? (Y)es/(N)o > ").upper() == "Y":
    # if they want to play call main again
    main()
  end() # if they don't play again then go to end func

def main():
  drink = ""
  waiting_for_selection = True
  while waiting_for_selection:
    clear()
    print("Welcome to BryBucks Coffee! Please select from our available menu:")
    show_menu()
    selected_drink = input("> ").upper().strip()
    if selected_drink == "O" or selected_drink == "OFF":
      print("Shutting down...")
      time.sleep(3)
      print("Goodbye")
      exit(0)
    elif selected_drink == "R":
      coffee_machine.report()
      cash_register.report()
      input("Press ENTER to continue...")
    elif selected_drink == "1":
      drink = "latte"
      waiting_for_selection = False
    elif selected_drink == "2":
      drink = "espresso"
      waiting_for_selection = False
    elif selected_drink == "3":
      drink = "cappuccino"
      waiting_for_selection = False
  if check_supply(drink) == True: # if sufficient, continue
    drink_price = return_cost(drink)
    display_drink_price = "${:,.2f}".format(drink_price)
    print(f"Please insert {display_drink_price}")
    count_coins_entered(drink_price)
    print(coffee_machine.make_coffee(brybucks_coffee_menu.find_drink(drink)))
    print("Enjoy!")
  return # return to main

main()
make_more()