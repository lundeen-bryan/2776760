def generate_password():
  #Password Generator Project
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters= int(input("How many letters would you like in your password?\n"))
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  password_list = ""
  total_characters = nr_numbers + nr_letters + nr_symbols
  password = ""

  if nr_letters != "":
    for ea in range(1,nr_letters+1):
      password_list += str(random.choice(letters))

  if nr_symbols != "":
    for ea in range(1,nr_symbols+1):
      password_list += str(random.choice(symbols))

  if nr_numbers != "":
    for ea in range(1,nr_numbers+1):
      password_list += str(random.choice(numbers))

  for ea in range(1,total_characters+1):
    password += str(random.choice(password_list))

  if password == "" or len(password) < 6:
    print("The data you entered is not enough for a secure password.")
  else:
    print(f"Your password is: {password}")
  return

print("Welcome to the PyPassword Generator!\n")
create_pass = input("Do you want to create a password? (y/n): ").capitalize()

if create_pass == "Y":
  generate_password()
else:
  exit(0)
