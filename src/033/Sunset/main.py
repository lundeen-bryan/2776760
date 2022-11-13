import requests
import datetime
import sys
import json
from urllib.request import urlopen
import os

sys.path.insert(0, "./src/")  # imports file_control.py from this parent folder
import _file_control as fc  # py file holding styles
import _clear_console as cc

dt = datetime.datetime

filepath = "./src/033/Sunset/"

def StartApp():
  # clear the console for status messages
  cc.clear()
  print("Welcome to Bryan's Sunset & ISS Finder!\n\n")

'''========================================='''
#=          Get My GPS Section                =
'''========================================='''
gps_url = "http://ipinfo.io/json"
print(f"Getting GPS Data from {gps_url}")

my_gps_data = json.load(urlopen(gps_url))
my_lat = my_gps_data["loc"].split(",")[0]
my_long = my_gps_data["loc"].split(",")[1]
print(f"Location: ({my_lat}, {my_long})")

#=========  End of Get My GPS Section   =======


"""========================================="""
# =             Sunrise Section                =
"""========================================="""

sunrise_url = "https://api.sunrise-sunset.org/json"
print(f"Getting sunrise data from {sunrise_url}")

sunset_params = {"lat": my_lat, "lon": my_long, "formatted": 0}
sunrise_response = requests.get(url=sunrise_url, params=sunset_params)
sunrise_response.raise_for_status()
sunrise_data = sunrise_response.json()
sunrise_split = str(dt.fromisoformat(str(sunrise_data["results"]["sunrise"]))).split(
    "+"
)
sunset_split = str(dt.fromisoformat(str(sunrise_data["results"]["sunset"]))).split("+")
time_now_split = str(dt.now()).split(".")

sunrise = sunrise_split[0]
sunrise_hour = int(sunrise.split(" ")[1].split(":")[0])
sunset = sunset_split[0]
sunset_hour = int(sunset.split(" ")[1].split(":")[0])
time_now = time_now_split[0]
time_now_hour = dt.now().hour

night = False
if time_now_hour >= sunset_hour or time_now_hour <= sunset_hour:
  night = True

sunset_summary = f"Time: {time_now}\n\nSunrise: {sunrise}\nSunset: {sunset}\n\n"
print(f"{sunset_summary}")
try:
  # write to file if it exists
  fc.write_file(filepath + "sunset.txt", sunset_summary, True)
except FileNotFoundError as e:
  print(f"An error occurred while writing to file: {e}: {filepath}sunset.txt\n")
  # else create the file
  fc.new_file(filepath + "sunset.txt", sunset_summary)
# end try

# =========  End of Sunrise Section  =======


"""========================================="""
# =         ISS Satelite Section               =
"""========================================="""

iss_url = "http://api.open-notify.org/iss-now.json"
print(f"Getting ISS Satelite data from {iss_url}")

iss_response = requests.get(iss_url)
iss_response.raise_for_status()

iss_data = iss_response.json()
iss_time = dt.fromtimestamp(iss_data["timestamp"])
iss_lat = iss_data["iss_position"]["latitude"]
iss_long = iss_data["iss_position"]["longitude"]

my_lat_distance = round(float(my_lat) - float(iss_lat), 2)
my_long_distance = round((float(my_long) * -1) - (float(iss_long) * -1), 2)

my_coordinates = f"({my_lat}, {my_long})"
iss_coordinates = f"({iss_lat}, {iss_long})"
my_position = f"Your Lat/Long position: {my_coordinates}\n"
iss_position = f"The iss position: {iss_coordinates}\n"
from_iss = f"Distance from the iss: \n\t\tLattitude: {my_lat_distance}\n\t\tLongitude: {my_long_distance}\n"

iss_summary = f"{my_position}\n{iss_position}\n{from_iss}\n"
print(f"{iss_summary}")

fc.write_file(filepath + "sunset.txt", iss_summary, False)
print(f"All data above has been written to: {filepath}sunset.txt")

print("Do you want to open the file? y/n")
user_input = input("> ")
if user_input == "y":
  os.system(f"code -r {filepath}sunset.txt")

print("Thank you for using Bryan's Sunsets & ISS Finder!")
# =========  End of ISS Satelite Section =======
