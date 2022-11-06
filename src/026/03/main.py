import pandas
import os

def clear():
  os.system("clear")

#TODO 1. Convert from a csv to dictionary to pandas DataFram
data_frame = pandas.DataFrame(pandas.read_csv("./src/026/03/nato_phonetic_alphabet.csv").to_dict())

#TODO 2. Get user input for a word
def main():
    print("Enter a word that you want to convert to the phonetic alphabet")
    user_input = input("> ").upper().strip()

    #TODO 3. From list of phonetic alphabet, translate word and print for user
    phonetic_translator = {row.letter: row.code for (index, row) in data_frame.iterrows()}
    translation = [phonetic_translator[letter] for letter in user_input]
    print(f"{translation}\n")

clear()
main()
while input("Would you like check another word? (Y)es/(N)o > ").upper() == "Y":
  # if they want to check again call main
  main()