# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import os

def clear():
  os.system("clear")


data = pandas.read_csv("./src/030A/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
    # comment:
    output_list = [phonetic_dict[letter] for letter in word]
  except KeyError as e:
    print("Sorry only letters can be entered.")
    generate_phonetic()
  else:
    # comment:
    print(output_list)
  # end try
  print(output_list)

generate_phonetic()