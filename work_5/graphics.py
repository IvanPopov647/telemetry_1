# 3: Создайте файл graphics.py и в нем реализуйте построение графиков (Вариант 6) Задача 1.


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,-0.9999, 10)                     # если x<-1 до -100
y = 4*x**4 + 12*x**3 + 13*x*2+8*x+1

fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label="y(x)")
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('1.png')                            # сохранить в файл 1.png