# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
"""
The position input asks for the column and row of the treasure
The variables below state that the first var is column and
the second var is row.
"""
col = int(position[0])
row = int(position[1])

#print(map[V - 1])
selected_row = map[row - 1] #column
selected_row[col - 1] = "💰" #row

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

