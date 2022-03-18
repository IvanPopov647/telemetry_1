# 3: Создайте файл graphics.py и в нем реализуйте построение графиков (Вариант 6)
# Задача 2 - Построение 3 графиков.

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5,-0.9999, 10)
x2 = np.linspace(-1, 0.9999, 10)
x3 = np.linspace(0, 5, 10)
y1 = 4 * x1 ** 4 + 12 * x1 ** 3 + 13 * x1 * 2 + 8 * x1 + 1
y2 = x2**0
y3 = (1-2*x3)/(x3**2+x3-2)

fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(x1, y1, color="black", label="y1(x)")      # функция y1(x), черная надпись y1(x)
ax.plot(x2, y2, color="red", label="y2(x)")  # функция y2(x), красная надпись y2(x)
ax.plot(x3, y3, color="green", label="y3(x)")   # функция y3(x), зеленая надпись y3(x)
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('3.png')                            # сохранить в файл 3.png
