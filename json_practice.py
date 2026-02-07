import json

my_score = {
    "player": "Dave",
    "points": 500,
}

with open("score.json", "w") as f:
    json.dump(my_score, f)
