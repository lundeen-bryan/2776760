"""
import sys
sys.path.insert(0, "./src/") # imports file_control.py from this parent folder

import file_control as fc

data_file = fc.read_file("025/weather_data.csv")
temperatures = []

def list_temperatures():
  for ea_row in data_file[1:]:
    x = 0
    s = ea_row.split(",")
    for ea_s in s:
      x += 1
      if (x % 2) == 0:
        temperatures.append(int(ea_s))

list_temperatures()
print(temperatures)
"""

import pandas as p

data_file = "./src/025/weather_data.csv"
data = p.read_csv(data_file)
temperatures = []

# print(data["temp"])
# print(type(data["temp"]))
data_dict = data.to_dict()

temp_list = data["temp"].to_list()
avg_temp = data["temp"].mean()
max_temp = data["temp"].max()
print(f"All the temperatures are: {temp_list}")
print(f"The average temperature is {avg_temp:.2f}")
print(f"The maximum temperature is {max_temp}")