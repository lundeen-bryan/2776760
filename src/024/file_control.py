import os
from os import path, sys

def read_file(file_name):
  file_name = os.path.join(sys.path[0], file_name)
  if path.isfile(file_name):
    with open(file_name, mode="r") as file:
      contents = file.readlines()
      return contents
  else:
    return f"{file_name} not found"

def write_file(file_name, new_text, overwrite=False):
  ovr = "a"
  if overwrite==True:
    ovr = "w"
  file_path = os.path.join(sys.path[0], file_name)
  if file_path.find("/.") != -1:
    file_path = file_name.replace("/.", "")
  if path.isfile(file_path):
    with open(file_path, mode=ovr) as file:
      file.write(f"{new_text}")
  else:
    new_file(file_name, new_text)

def new_file(file_name, new_text):
  file_path = os.path.join(sys.path[0], file_name)
  if file_path.find("/.") != -1:
    file_path = file_name.replace("/.", "")
  with open(file_path, mode="w") as file:
    file.write(f"{new_text}")
  print(f"created: {file_path}")
