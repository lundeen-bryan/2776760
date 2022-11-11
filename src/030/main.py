try:
  # comment: open a file
  file = open("./src/030/a_file.txt", "r")
  a_dictionary = {"key": "value"}
  print(a_dictionary["key"])
except FileNotFoundError as e:
  file = open("./src/030/a_file.txt", "w")
  file.write("Something")
  print(f"{e} File will be created.")
except KeyError as k:
  print(f"The key {k} does not exist.")
else:
  content = file.read()
  print(content)
finally:
  file.close()
  print("File was closed.")
# end try

