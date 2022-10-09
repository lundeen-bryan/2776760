#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

loop_msg = '''
  Do you want to flip again?
  Type Y for Yes and N for No to continue...
  '''

count = 2
while (count <= 2):
  count -=1
  rand_num = random.randint(0,1)
  if rand_num == 0:
    print("\nTails")
  else:
    print("\nHeads")
  if count <2:
    loop_again = input(loop_msg).capitalize()
    if loop_again == "N":
      count = 3
