# 3: Создайте файл graphics.py и в нем реализуйте построение графиков (Вариант 6) Задача 2.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,0.9999, 10)                     # если 1 =< x < 1
y = (1-2*x)/(x**2+x-2)

fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label="y(x)")
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('2.png')                            # сохранить в файл 1.png