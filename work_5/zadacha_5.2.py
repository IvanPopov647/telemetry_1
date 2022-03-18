#2: Создайте модуль. В нем создайте функцию, которая принимает список и
#возвращает из него случайный элемент. Если список пустой функция должна
#вернуть None. Проверьте работу функций в этом же модуле.

import random

nums = input('Введите список для проверки:')


def get_random_int(numbers):
    if len(numbers) == 0:
        return None
    return random.choice(numbers)

if __name__ == "__main__":
    print(get_random_int(nums))
