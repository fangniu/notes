# -*- coding: utf-8 -*-

from random import randint


def shuffle(array):
    n = len(array)
    for i in range(n-1, -1, -1):
        j = randint(0, i)
        if j != i:
            array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    l1 = list(range(10))
    shuffle(l1)
    print(l1)

