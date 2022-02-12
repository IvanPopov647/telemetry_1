revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
number_of_employees = int(input('Введите количество сотрудников: '))
profit = revenue - costs
rent = profit / revenue
salary = profit / number_of_employees
while True:
    if revenue > costs:
        print(f'Финансовая прибыль фирмы: {profit:.2f}')
        print(f'Соотношение прибыли к выручке: {rent:.2f}')
        print(f'Прибыль фирмы в расчете на одного сотрудника: {salary:.2f}')
        break
    elif revenue < costs:
        print(f'Выручка меньше издержек : {profit:.2f}, Убыток фирме')
        break
    else:
        print(f'Выручка и издержки одинаковы, прибыль равна {profit:.2f}')
        break