# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
"""
For each name check the # of occurances
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times

Scores < 10 or > 90 return
"Your score is **x**, you go together like coke and mentos."
Scores between 40 - 50 return
"Your score is **y**, you are alright together."
Else "Your score is **z**."
"""
#convert names to lowercase
name_lower = name1.lower() + name2.lower()

# each name count letters
T = name_lower.count("t")
R = name_lower.count("r")
U = name_lower.count("u")
E1 = name_lower.count("e")

L = name_lower.count("l")
O = name_lower.count("o")
V = name_lower.count("v")
E2 = name_lower.count("e")

# add up both columns
true = T + R + U + E1
love = L + O + V + E2

#convert each total to a string
total_str = str(true) + str(love)

#convert the string to int
love_score = int(total_str)

#print messages based on Values
if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >=40 and love_score <=50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
