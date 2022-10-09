import random

count = 0
while (count < 2):
  rand_num = random.random() * 5
  print(rand_num)
  count +=1
  if count >1:
    loop_again = input("Do you want to get another random number? Y/N")
    if loop_again == "Y":
      count = count - 1

