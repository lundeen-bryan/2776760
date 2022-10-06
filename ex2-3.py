# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# return num yrs til 90 as floor
years = 90 - int(age)
# return num of months til bmonth as floor
months = years * 12
# return num of weeks til bday
weeks = years * 52
# return num of days til bday as floor
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left until you are 90 yrs old.")