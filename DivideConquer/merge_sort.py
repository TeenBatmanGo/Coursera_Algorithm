
def merge_sort(x):
    n = len(x)
    if n == 1:
        return x
    mid = round(n/2)
    left_x, right_x = x[:mid], x[mid:]
    left_sorted = merge_sort(left_x)
    right_sorted = merge_sort(right_x)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    n = len(left)+len(right)
    output = []
    i, j = 0, 0
    for k in range(n):
        if int(left[i]) <= int(right[j]):
            output.append(left[i])
            i += 1
            if i > len(left)-1:
                output.extend(right[j:])
                break
        else:
            output.append(right[j])
            j += 1
            if j > len(right)-1:
                output.extend(left[i:])
                break
    return output


if __name__ == '__main__':
    arr = ['2', '5', '1', '2', '3', '4', '7', '0']
    print('Sorted:', merge_sort(arr))