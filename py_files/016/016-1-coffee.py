from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_brybucks = Menu()
items_brybucks = MenuItem()

return_drink = menu_brybucks.find_drink("cappuccino")
drink_cost = return_drink.cost
print(f"The cost is {drink_cost}")