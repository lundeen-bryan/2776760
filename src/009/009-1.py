student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

#TODO-2: Write your code below to add the grades to student_grades.👇
def create_dictionary(starting_dictionary, list_name, new_dictionary):
  list_name = list(starting_dictionary.keys())
  new_dictionary = {}
  for ea in list_name:
    if starting_dictionary[ea] >= 91 and starting_dictionary[ea] <= 100:
      new_dictionary[ea] = ea + " scored: " + str(starting_dictionary[ea]) + " - Outstanding!"
    elif starting_dictionary[ea] >= 81 and starting_dictionary[ea] <= 90:
      new_dictionary[ea] = ea + " scored: " + str(starting_dictionary[ea]) + " - Exceeds Expectations!"
    elif starting_dictionary[ea] >= 71 and starting_dictionary[ea] <= 80:
      new_dictionary[ea] = ea + " scored: " + str(starting_dictionary[ea]) + " - Aceptable."
    elif starting_dictionary[ea] <=70:
      new_dictionary[ea] = ea + " scored: " + str(starting_dictionary[ea]) + " - Fail!"
  return new_dictionary

#  print(ea + ": " + str(student_scores[ea]))
student_grades = create_dictionary(starting_dictionary=student_scores, list_name="key_list", new_dictionary="final_grades")

# 🚨 Don't change the code below 👇
print(student_grades)
#print("\n")
#print(create_dictionary(starting_dictionary=student_scores, list_name="key_list", new_dictionary="final_grades"))

##===========================================================================================
## Date: .............. 2022-10-13
## Program: ........... 009-1.py
## Website: ........... none
## Description: ....... create dictionary challenge holding student grades
## Installs to: ....... py_files/009
## Compatibility: ..... Python 3
## Contact Author: .... lundeen-bryan
## Copyright © ........ n/a 2022. All rights reserved.
## Called by: ......... n/a
## Called to: ......... n/a
## Parameters: ........ n/a
##
## Notes:
## I wanted to use my own print statement but that's not part of the requirements for the
## challenge.
##
##===========================================================================================
