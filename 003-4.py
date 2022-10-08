# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# total based on size
if size == "S":
    size_total = 15
elif size == "M":
  size_total = 20
else:
  size_total = 25

#total of the pepperoni item
if add_pepperoni == "Y" and size == "S":
  pep_total = 2
elif add_pepperoni == "Y" and size == "M" or size == "L" and add_pepperoni =="Y":
  pep_total = 3
else:
  pep_total = 0

#total of the cheese item
if extra_cheese == "Y":
  cheese_total = 1
else:
  cheese_total = 0

#total all items
order_total = size_total + pep_total + cheese_total

#show  item total
print(f"Your final bill is: ${order_total}.")