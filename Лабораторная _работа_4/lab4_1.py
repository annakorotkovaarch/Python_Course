import json


def task() -> float:
    ds = json.load(open("input.json", "r"))

    result = 0.0
    for item in ds:
        score = item['score']
        weight = item['weight']
        result += score * weight

    return round(result, 3)


print(task())