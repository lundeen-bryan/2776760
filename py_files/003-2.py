# 🚨 Don't change the code below 👇
from ast import match_case
from tokenize import Comment


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Calculate the BMI """

numerator  = float(height) ** 2
denominator  = float(weight)
result = denominator / numerator
bmi = int(result)

# set a const value for the sentence """

SENTENCE = f"Your BMI is {bmi}, you "

# use a match statement """

if height <= 0 or weight <= 0:
  print("Please enter both height and weight.")
elif float(bmi) < 19:
  print(SENTENCE + "are underweight.")
elif float(bmi) in range(19, 24):
  print(SENTENCE + "have a normal weight.")
elif float(bmi) in range(25, 29):
  print(SENTENCE + "are slightly overweight.")
elif float(bmi) in range(30, 34):
  print(SENTENCE + "are obese.")
elif float(bmi) > 34:
  print(SENTENCE + "are clinically obese.")
