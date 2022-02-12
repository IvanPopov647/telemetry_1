a = float(input('Введите число км: '))
b = float(input('Введите конечную цель: '))
day = 1

if a > b:
    print(day)
while True:
    if a <= 0 or b <= 0:
        print('Результат должен быть больше нуля.')
    else:
        while a < b:
            a = a + a*0.1
            day += 1
        print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.')
        break