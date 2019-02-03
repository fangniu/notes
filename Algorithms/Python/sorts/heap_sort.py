# -*- coding: utf-8 -*-

import random


def heapify(unsorted, index, heap_size):
    largest_index = index
    left_index = 2*index + 1
    right_index = 2*index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest_index]:
        largest_index = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest_index]:
        largest_index = right_index
    if largest_index != index:
        unsorted[index], unsorted[largest_index] = unsorted[largest_index], unsorted[index]
        heapify(unsorted, largest_index, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)
    # 构造初始堆。将给定无序序列构造成一个大顶堆；从最后一个非叶子结点开始（叶结点自然不用调整)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    # 将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素。如此反复进行交换、重建、交换。
    for i in range(n-1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


if __name__ == '__main__':
    for _ in range(5):
        array = list(range(20))
        random.shuffle(array)
        print('before:', array)
        heap_sort(array)
        print('after:', array)
        print('=======================')
