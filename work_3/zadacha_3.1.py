def div(*args):

    try:
        arg1 = int(input("Введите делимое "))
        arg2 = int(input("Введите делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "Неправильный делитель! Вы не можете использовать ноль в качестве делителя."

    return res

    """
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Неправильный номер! Делитель не может быть равен нулю")
    """


print(f'result  {div()}')