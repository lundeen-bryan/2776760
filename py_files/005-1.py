# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# heights input will be 180 124 165 173 189 169 146
ea_student = 0
ea_height = 0

for x in student_heights:
  ea_student +=1
  ea_height +=x

avg_height = round(ea_height / ea_student,2)

print(f"The average student is {avg_height} meters tall.")