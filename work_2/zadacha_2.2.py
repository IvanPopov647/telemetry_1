el_count = int(input("Введите количество элементов списка "))
list = []
i = 0
el = 0
while i < el_count:
    list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(list)/2)):
        list[el], list[el + 1] = list [el + 1], list[el]
        el += 2
print(list)