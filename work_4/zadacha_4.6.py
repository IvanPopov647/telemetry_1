import re

sp = {}
with open('Text_6.txt', 'r') as file_obj:
    text = file_obj.read()
    file_obj.seek(0)

    for i in file_obj:
        i_items = i.split(': ')
        chas = re.findall(r"\d+", i_items[1])
        sp.update({i_items[0]: sum([int(i) for i in chas])})

print(f"Словарь:\n{sp}")