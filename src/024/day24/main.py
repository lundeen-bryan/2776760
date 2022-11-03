import os
from os import path, sys

def read_file(file_name):
  file_name = os.path.join(sys.path[0], file_name)
  if path.isfile(file_name):
    with open(file_name) as file:
      contents = file.read()
      return contents
  else:
    return f"{file_name} not found"

def write_file(file_name, new_text):
  file_name = os.path.join(sys.path[0], file_name)
  if path.isfile(file_name):
    with open(file_name, mode="a") as file:
      file.write(f"\n{new_text}")
  else:
    new_file(file_name, new_text)

def new_file(file_name, new_text):
  file_name = os.path.join(sys.path[0], file_name)
  with open(file_name, mode="w") as file:
    file.write(f"\n{new_text}")

def main():
  write_file("my_file.txt","Here's new text")
  print(read_file("my_file.txt"))

main()