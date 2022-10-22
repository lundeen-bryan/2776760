def encrypt(message_to_code, shift_number):
  # shift characters in the message
  result = ""
  for letter in range(len(message_to_code)):
    character = message_to_code[letter]
    # encrypt uppercase letters
    if ord(character) >= 65 and ord(character) <= 91:
        result += chr((ord(character) + shift_number - 65) % 26 + 65)
    # encrypt lowercase letters
    elif ord(character) >= 97 and ord(character) <= 122:
      result += chr((ord(character) + shift_number - 97) % 26 + 97)
    # no change if non alphabet characters
    else:
      result += str(message_to_code[letter])
  return result

# display ascii art
from art import logo
print(logo)

# check the above function
game_end = False
while not game_end:
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n(enter a negative number to decode)\n"))
  print(f"Plain Text: {text}")
  print(f"Shift pattern: {shift}")
  print("Cipher: " + encrypt(message_to_code=text, shift_number=shift))
  start_again = input("\nDo you want to encode/decode another message? \nType Y for yes and N for no to continue...").upper()
  if start_again == "N" or start_again == "NO":
    print("Goodbye.")
    game_end = True

##===========================================================================================
## Date: .............. 2022-10-13
## Program: ........... 008-3-cipher-2.py
## Website: ........... none
## Description: ....... Ceaser Cipher
## Installs to: ....... py_files/008
## Compatibility: ..... Python 3
## Contact Author: .... lundeen-bryan
## Copyright © ........ n/a 2022. All rights reserved.
## Called by: ......... none
## Called to: ......... none
## Arguments: ......... none
##
## Notes:
## Use the unicode value of ea letter in the alphabet, when the position is > the number
## of letters in the alphabet, mod by the number of letters to get the remainder, then
## again return the unicode value of that letter. By default it shifts left, to shift
## right, enter a negative number for the shift value.
##
##===========================================================================================
