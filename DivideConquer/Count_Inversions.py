
import base
from merge_sort import merge_sort


def count_inversions(x):
    n = len(x)
    if n == 1:
        return x, 0
    mid = round(n/2)
    left_x, right_x = x[:mid], x[mid:]
    B, left_cnt = count_inversions(left_x)
    C, right_cnt = count_inversions(right_x)
    split_cnt = count_split_inversions(x, B, C)
    return merge_sort(x), left_cnt+right_cnt+split_cnt


def count_split_inversions(x, B, C):
    n = len(B) + len(C)
    i, j, cnt = 0, 0, 0
    for k in range(n):
        if int(C[j]) < int(B[i]):
            cnt += len(B)-i
            j += 1
            if j > len(C)-1:
                break
        else:
            i += 1
            if i > len(B)-1:
                break
    return cnt


if __name__ == '__main__':
    arr = base.load_Integer_Array()
    print(count_inversions(arr)[1])