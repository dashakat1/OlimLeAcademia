import json

with open("input.txt", "r") as f:
    sales = json.load(f)

overall_sales = {}

for _, catalog in sales.items():
    for product, number in catalog.items():
        try:
            overall_sales[product] += int(number)
        except KeyError:
            overall_sales[product] = int(number)

with open("output.txt", "w") as f:
    json.dump(overall_sales, f)
