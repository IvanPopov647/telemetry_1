file = {'Student 1': 4, 'Student 2': 1, 'Student 3': 7, 'Student 4': 9, 'Student 5': 5, 'Student 6': 0, 'Student 7': 4, 'Student 8': 1, 'Student 9': 10, 'Student 10': 11}
try:
    file_obj = open("Text_3.txt", 'w')
    for familia, stipendia in file.items():
        file_obj.write(familia + ':' + str(stipendia) + "\n")
except IOError:
    print("Ошибка")
finally:
    file_obj.close()
summa = 0
stip = 0
fam = []
with open("Text_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 5:
            fam.append(tokens[0])
        summa += int(tokens[1])
        stip += 1
srednee = summa / stip
print(f"Фамилии: {fam}")
print(f"Среднее: {srednee}")