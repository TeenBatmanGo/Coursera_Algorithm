
# For testing algorithms.

import numpy as np

def choose_pivot_random(start, end):
    return np.random.choice(range(start, end))

def swap(x, i, j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp

def partition(x, start, end, p):
    pivot = x[p]
    swap(x, start, p)
    i = start
    for j in range(start, end):



def quick_sort(x, start, end, choose_pivot=choose_pivot_random):
    if end - start <= 1:
        return None
    p = choose_pivot(start, end)
    partition_ind = partition(x, start, end, p)
    quick_sort(x, start, partition_ind, choose_pivot)
    quick_sort(x, partition_ind+1, end, choose_pivot)
    return None


if __name__ == '__main__':
    a = [2, 3, 2, 4, 1, 1]
    quick_sort(a, 0, len(a))
    print(a)