def format_name(l_name, f_name):
  f_name = str(f_name).title()
  l_name = str(l_name).title()
  return f"{f_name} {l_name}"

blank_name = True
first = ""
last = ""

while blank_name:
  if first == "":
    first = input("Enter your first name: ")
  if last == "":
    last = input("Enter your last name: ")
  if first != "" and last != "":
    blank_name = False
  else:
    print("Please enter both your first and last name to continue.")

  print("\nYour full name is:\n")
  print(format_name(f_name=first, l_name=last))
