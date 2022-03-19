import matplotlib.pyplot as plt
import numpy as np
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третий число:'))
x = np.linspace(-100,100, 100)
y = a*x**2 + b*x + c
fig, ax = plt.subplots()
ax.plot(x, y, color="blue", label="y(x)")
ax.set_xlabel("x")                              # подпись у горизонтальной оси х
ax.set_ylabel("y")                              # подпись у вертикальной оси y
ax.legend()                                     # показывать условные обозначения

plt.show()                                      # показать рисунок
fig.savefig('График квадратичной функции.png')                            # сохранить в файл График квадратичной функции.png