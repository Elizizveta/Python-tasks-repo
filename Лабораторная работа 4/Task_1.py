# TODO решите задачу
filename = 'input.json'
import json
def task(json_file) -> float:
    ...
    with open(json_file) as file:
        data = json.load(file)
        product_sum = sum(entry["score"] * entry["weight"] for entry in data)
        return round(product_sum, 3)

print(task(filename))



