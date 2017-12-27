import numpy as np
from select import select

def choose_pivot_random(x, start, end):
    from numpy.random import choice
    np.random.seed(1)
    return choice(range(start, end))

def choose_pivot_first(x, start, end):
    return start

def choose_pivot_last(start, end):
    return end-1

def choose_pivot_median3(x):
    first, midd, last = x[0], x[((len(x)-1)/2).__trunc__()], x[-1]
    output = select([first, midd, last], 1)
    ind = x.index(output)
    return ind


def partition1(x, start, end, p):
    pivot = x[p]
    swap(x, start, p)
    i = start
    for j in range(start, end-1):
        if int(x[j+1])<=int(pivot):
            swap(x, j+1, i+1)
            i += 1
    swap(x, start, i)
    return i


def partition2(x, start, end, p):
    pivot = x[p]
    swap(x, start, p)
    i = start+1
    j = end-1
    while True:
        while i < end and x[i] <= pivot:
            i += 1
        while j > start and x[j] >= pivot:
            j -= 1
        if i >= j:
            break
        swap(x, i, j)
    swap(x, start, i-1)
    return i-1



def swap(x, i, j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp


# Need to sort x inplace, so we need to specify start and end for recursion.
cnt = 0
def quick_sort(x, start, end, choose_pivot=choose_pivot_random, partition=partition1):
    global cnt
    n = end - start
    if n<=1:
        return None
    p = choose_pivot(x, start, end)
    partition_ind = partition(x, start, end, p)
    quick_sort(x, start, partition_ind, choose_pivot)
    quick_sort(x, partition_ind+1, end, choose_pivot)
    return None


if __name__ == '__main__':
    a = [6, 2, 5, 4, 1, 1, 2, 2, 3]
    print('Before:', a)
    quick_sort(a, 0, len(a), choose_pivot_random, partition2)
    print('After:', a)