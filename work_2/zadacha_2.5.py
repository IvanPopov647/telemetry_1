list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {list}")
digit = int(input("Введите число (111 - выход) "))
while digit != 111:
    for el in range(len(list)):
        if list[el] == digit:
            list.insert(el + 1, digit)
            break
        elif list[0] < digit:
            list.insert(0, digit)
        elif list[-1] > digit:
            list.append(digit)
        elif list[el] > digit and list[el + 1] < digit:
            list.insert(el + 1, digit)
    print(f"текущий список - {list}")
    digit = int(input("Введите число "))