from array import *
from random import *


def filling_array(mas: array, size: int):
    for i in range(size):
        mas.append(randint(1, 20))
    return array


def print_array(mas: array):
    for i in range(len(mas)):
        print(mas[i])


def is_sorted_ascending_order(mas: array):
    for i in range(len(mas) - 1):
        if mas[i] >= mas[i + 1]:
            return 0
    return 1


def is_sorted_descending_order(mas: array):
    for i in range(len(mas) - 1):
        if mas[i] <= mas[i + 1]:
            return 0
    return 1
