#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill_total = input("What was the total bill? $")
tip = input("Enter the tip percent, but without a percent sign, e.g. 10, 12, 15: ")
tip = 1 + (int(tip) / 100)
bill_total = float(bill_total) * tip
people = input("How many people to split the bill?")
bill_split = float(bill_total) / int(people)
result = "${:,.2f}".format(bill_split)
print("Each person should pay: " + result)
