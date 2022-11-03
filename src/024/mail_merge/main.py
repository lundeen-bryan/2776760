import sys
sys.path.insert(0, "./src/024/") # imports file_control.py from this parent folder

import file_control as fc

STARTING_LETTER_PATH = "../024/mail_merge/Input/Letters/starting_letter.txt"
OUTPUT_FOLDER = "./src/024/mail_merge/Output/ReadyToSend/"
NAMES_PATH = "../024/mail_merge/Input/Names/invited_names.txt"

def replace_greeting(new_recipient, index):
    letter_text = fc.read_file(STARTING_LETTER_PATH)
    letter_text[0] = f"Dear {new_recipient},\n" # 0 is always the greeting
    for line in letter_text:
        fc.write_file(f"{OUTPUT_FOLDER}letter_for_{new_recipient}.txt",line,False)
    if index == 0:
        plural = "letter is"
    else:
        plural = "letters are"
    print(f"{index+1} {plural} done.")

def get_names():
    names = fc.read_file(NAMES_PATH)
    return names

def main():
    new_names = get_names()
    names_count = len(new_names)
    for ea in range(names_count):
        replace_greeting(new_names[ea].strip(), ea)

main()