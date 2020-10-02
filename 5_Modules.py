import sys          # from sys import argv  then argv = sys.argv
import os
from math import *  # usually need to use only import, because to avoid name conflicts

print('terminal arguments')
for i in sys.argv:
    print(i)

print('\n\n Value PYTHONPATH contains', sys.path, '\n')

print(os.getcwd())      # current catalog


n = int(input("Введите диапазон:- "))
p = [2, 3]
count = 2
a = 5
while (count < n):
    b = 0
    for i in range(2, a):
        if (i <= sqrt(a)):
            if (a % i == 0):
                print("a neprost", a)
                b = 1
            else:
                pass

        if (b != 1):
            print("a prost", a)
            p = p + [a]

        count = count + 1
        a = a + 2

print(p)

if __name__ == '__main__':
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')
