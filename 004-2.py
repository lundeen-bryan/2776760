# Split string method
from dataclasses import replace


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
from remove_spaces_mod import remove_spaces

remove_spaces(names_string)

names = names_string.split(", ")

max_names = len(names)

result = random.randint(0,max_names)

print(f"{names[result]} will pay the bill today. ")
