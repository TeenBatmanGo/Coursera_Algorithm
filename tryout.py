# Try some simple algorithms


# invert using recursion
def invert(x):
    n = len(str(x))
    if n <= 1:
        return x
    return str(x)[-1]+invert(str(x)[:-1])


# a = 12
# result = invert(a)
# print(result)




# Hanoi Tower
def move(n, a, buffer, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1, a, c, buffer)
    move(1, a, buffer, c)
    move(n-1, buffer, a, c)


# move(2, 'A', 'B', 'C')




# Get the median of two equal-length sorted arrays.
def get_median(x, y):
    n = len(x)
    if n == 2:
        left = max(x[0], y[0])
        right = min(x[1], y[1])
        return (left+right)/2
    mid = (n / 2).__trunc__()
    if n%2 == 0:
        low, high = n//2-1, n//2
        mid_x = (x[low] + x[high]) / 2
        mid_y = (y[low] + y[high]) / 2
        mid1, mid2 = mid, mid
    else:
        mid_x, mid_y = x[mid], y[mid]
        mid1, mid2 = mid, mid+1
    if mid_x == mid_y:
        return mid_x
    elif mid_x < mid_y:
        return get_median([mid_x]+x[mid2:], y[:mid1]+[mid_y])
    else:
        return get_median(x[:mid1]+[mid_x], [mid_y]+y[mid2:])


# xx = [6, 100, 120, 200, 210]
# yy = [2, 33, 103, 110, 117]
# result = get_median(xx, yy)
# import numpy as np
# print(result, np.median(xx+yy))