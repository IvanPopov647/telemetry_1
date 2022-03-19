#3. Напишите программу для решения квадратного уравнения вида ax2+bx+c.
#Вывести график квадратного уравнения. Коэффициенты a, b, c запросить у
#пользователя. Использовать обработку исключений.


import math

def devizion(a, b, c):

    try:
        D = (b**2)-4*a*c
        x1 = (-b + math.sqrt(D)) / 2 * a
        x2 = (-b - math.sqrt(D)) / 2 * a
    except TypeError:
        D = f'{a},{b},{c} Переменная должна быть числом'
    except UnboundLocalError:
        x1 = 'Корня нет'
        x2= 'Корня нет'
    except ValueError:
        x1 = 'Корня нет'
        x2 = 'Корня нет'

    return D, x1, x2


print(devizion(int(input("Введите a:")), int(input("Введите b: ")), int(input("Введите c:"))))

