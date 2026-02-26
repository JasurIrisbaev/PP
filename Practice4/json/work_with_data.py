import json

with open("../sample-data.json") as f:
    data=json.load(f)

for s in data["students"]:
    print(s["name"])