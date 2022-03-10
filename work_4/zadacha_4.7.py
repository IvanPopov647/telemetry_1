import json
sp = []

with open('Text_7.txt', 'r') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    profit_sum = 0

    for row in file:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_sum += profit
    sp.append(profits)
    sp.append({'average_profit': (profit_sum / len(profits))})

with open('Text_7.json', 'w') as json_file:
    json.dump(sp, json_file)

json_sp = json.dumps(sp)

print(f"Фирмы:\n{text}\n")
print(f"Выручка:\n{sp}\n")
print(f"json-объект:\n{json_sp}")