import pandas as pd

data_file = "./src/025B/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
#get a data frame
data = pd.read_csv(data_file)

# count of ea color
squirrel_colors = data["Primary Fur Color"].value_counts()

# print count if ea color
print(squirrel_colors)
