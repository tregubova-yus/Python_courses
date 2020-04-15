#coding=UTF-8
"""
Среднее среди 100 случайных чисел
"""
import numpy as np 
import random

print('Введите диапазон целых чисел:')

a = input()
b = input()

lst = np.random.randint(a, b, 100)

print('Сгенерированный ряд: {0}'.format(lst))
print('Среднее значение: {0}'.format(lst.mean()))