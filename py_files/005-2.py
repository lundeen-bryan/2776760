# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#sample scores
"""
78 65 89 86 55 91 64 89
"""
highest_score = 0
for x in student_scores:
  if x > highest_score:
    highest_score = x
print(f"The highest_score is {highest_score}")
