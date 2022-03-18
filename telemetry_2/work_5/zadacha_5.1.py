# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
import os


minimum_number = 1
maximum_number = 10

#Функция, создающая папки
def make_dirs():
    for new_dir_i in range(minimum_number, maximum_number):
        new_dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(new_dir_i))
        os.mkdir(new_dir_path)

#Функция, удаляющая папки
def remove_dirs():
    for i in range(minimum_number, maximum_number):
        path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(path)


if __name__ == "__main__":
    make_dirs()
    remove_dirs()