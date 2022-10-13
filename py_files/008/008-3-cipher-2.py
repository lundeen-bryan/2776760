def encrypt(message_to_code, shift_number, code_type):
  # transverse the message
  result = ""
  if code_type == "encode":
    for letter in range(len(message_to_code)):
      character = message_to_code[letter]
      # encrypt uppercase letters
      if (character.isupper()):
        result += chr((ord(character) + shift_number - 65) % 26 + 65)
      # encrypt lowercase letters
      else:
        result += chr((ord(character) + shift_number - 97) % 26 + 97)
    return result
  else:
    for letter in range(len(message_to_code)):
      character = message_to_code[letter]
      # encrypt uppercase letters
      if (character.isupper()):
        result += chr((ord(character) + shift_number - 65) % 26 - 65)
      # encrypt lowercase letters
      else:
        result += chr((ord(character) + shift_number - 97) % 26 - 97)
    return result

# check the above function

#message_to_code = "zulu"
message_to_code = "dypy"
shift_number = 4
# code_type = "encode"
code_type = "decode"

print(f"Plain Text: {message_to_code}")
print(f"Shift pattern: {shift_number}")
print("Cipher: " + encrypt(message_to_code, shift_number, code_type))
