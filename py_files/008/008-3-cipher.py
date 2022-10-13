alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def ceasar(message_to_code, shift_number, code_type):
  #titled ceasar for ceasar's cipher
  encoded_message = ""
  for letter in message_to_code:
    if letter in alphabet:
      position = alphabet.index(letter)
      if code_type == "encode":
        new_position = position + shift_number
      else: #decode
        new_position = position - shift_number
      new_letter = alphabet[new_position]
      encoded_message += new_letter
    else:
      encoded_message += letter
  return f"The {code_type}d text is {encoded_message}"

from art import logo
print(logo)

game_end = False
while not game_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % len(alphabet) #using 26 letters plus a space

  if direction == "encode" or direction == "decode":
    coded = ceasar(message_to_code=text, shift_number=shift, code_type=direction)
    print(coded)
  else:
    print(f"You can only choose to encode or decode a message. You can't choose '{direction}.'")
  start_again = input("Do you want to encode/decode another message? \nType Y for yes and N for no to continue...").capitalize
  if start_again == "No":
    game_end = True
    print("Goodbye.")
