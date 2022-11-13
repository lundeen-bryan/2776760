import csv
import json


def make_json(csv_path, json_path):
    data = {}

    with open(csv_path, "r", encoding="utf-8", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")

        for row in csv_reader:
            key = row["French"]
            data[key] = row

    with open(json_path, "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(data, sort_keys=True, indent=4))


csv_path = "./src/031/data/french_words.csv"
json_path = "./src/031/data/french_words.json"

if __name__ == "__main__":
    make_json(csv_path, json_path)
