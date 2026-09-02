import os
import json

# 1. Finds the folder where main.py lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Glues the folder path and the filename together
file_path = os.path.join(script_dir, "high-jump-log.json")

def loadData():
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        pass

def saveData(data):
    with open(file_path, "w") as file:
        json.dump(data, file)
