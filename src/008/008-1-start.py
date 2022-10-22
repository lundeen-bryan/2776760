#Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
"""
def greet():
  print("Hello, world! 1")
  print("Hello, world! 2")
  print("Hello, world! 3")

#greet()

def greet_person(name):
  print(f"Hello,{name}!")
  print(f"How do you do {name}?")

greet_person("Angela")
"""
def greet_with(name, location):
  print(f"Hello, {name}!")
  print(f"What's it like in {location}?")

user_name = input("Please enter your name: ")
user_loc = input("Please enter your location: ")

greet_with(name=user_name, location=user_loc)
