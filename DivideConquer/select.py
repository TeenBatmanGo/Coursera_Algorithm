from merge_sort import merge_sort


def partition(x, start, end, p):
    pivot = x[p]
    swap(x, start, p)
    i = start
    for j in range(start, end-1):
        if int(x[j+1])<=int(pivot):
            swap(x, j+1, i+1)
            i += 1
    swap(x, start, i)
    return i

def swap(x, i, j):
    temp = x[i]
    x[i] = x[j]
    x[j] = temp


def choose_pivot_determ(x, start, end):
    from math import ceil
    n = end-start
    m = ceil(n/5)
    x_med = []
    for i in range(m):
        x_sub = x[start:end][i*5:(i+1)*5]
        n_x = len(x_sub)
        x_sub_sorted = merge_sort(x_sub)
        x_sub_med = x_sub_sorted[round(n_x/2)]
        x_med.append(x_sub_med)
    return select(x_med, (m/2).__trunc__(), 0, len(x_med), choose_pivot_determ)


# Inplace implementation
def select(x, k, start, end, choose_pivot=choose_pivot_determ):
    if end-start<=1:
        return x[start]
    p = choose_pivot(x, start, end)
    if choose_pivot==choose_pivot_determ:
        p = x.index(p)
    partition_ind = partition(x, start, end, p)
    if partition_ind-start>k:
        return select(x, k, start, partition_ind, choose_pivot)
    elif partition_ind-start==k:
        return x[partition_ind]
    else:
        return select(x, k-partition_ind+start-1, partition_ind+1, end, choose_pivot)


if __name__ == '__main__':
    import numpy as np
    a = [1, 1, 2, 3, 1, 2, 4]
    print('test:', select(a, 3, 0, len(a), choose_pivot_determ))
    print('real:', np.sort(np.array(a).astype('int64'))[3])