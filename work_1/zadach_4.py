number = int(input('Введите число: '))
max_number = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_number:
        max_number = number % 10
    number = number // 10

print('Самая большая цифра в числе: ', max_number)
