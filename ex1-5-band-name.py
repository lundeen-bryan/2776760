# Written for Python 2.7 not v3.x
#1. Create a greeting for your program.
new_line = '\n'
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
print(new_line)
city = raw_input("What's the name of the city you grew up in? ")
#3. Ask the user for the name of a pet.
print(new_line)
pet = raw_input("What's the name of your pet? ")
#4. Combine the name of their city and pet and show them their band name.
print(new_line)
print("Your band name is: " + city + " " + pet + ".")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
