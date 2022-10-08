print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
enter_choice = input(
  '''
  You are standing at the edge of a jungle.
  Do you want to enter?
  Enter Y for yes and N for no to continue...
  ''')
if enter_choice == "N":
  print(
    '''
    Since you didn't enter the jungle,
    one of the other pirates stabbed you in the back.
    '''
  )
  exit("Game Over.")
else:
  print("You have entered the jungle.")

find_tree = input(
  '''
  Your map says to find the crooked tree.
  Do you want to search to the left or to the right?
  Enter L or R to continue...
  '''
)
if find_tree == "L":
  print(
    """
    As you proceed to the left, you notice a big totem pole in the middle of a clearing.
    """
  )
  totem_pole = input(
    '''
    Do you want to dig at the foot of the totem pole for treasure?
    Enter Y for yes and N for no to continue...
    '''
  )
  if totem_pole == "Y":
    print(
      '''
      The cannibals caught you denigrating their idol.
      Tonight you will be their dinner.
      '''
    )
    exit("Game Over.")
  else:
    print(
      '''
      Because you honored their idol,
      the cannibals have shown you where the crooked tree is.
      You will now proceed to the right.
      '''
    )
dig_here = input(
  '''
  You found the crooked tree.
  Do you want to start digging here?
  Enter Y for yes and N for no to continue...
  '''
)
if dig_here == "Y":
  print(
    '''
    You found the treasure!
    You Win!!
    '''
  )
else:
  print(
    '''
    Since you didn't dig,
    one of the other pirates stabbed you in the back.
    '''
  )
