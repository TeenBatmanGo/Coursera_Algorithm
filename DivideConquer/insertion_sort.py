
def insertion_sort(x):
    n = len(x)
    for i in range(1, n):
        current = x[i]
        j = i - 1
        while x[j] > current and j >= 0:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = current
    return x



if __name__ == '__main__':
    testcase = [4, 3, 2, 1]
    result = insertion_sort(testcase)
    print(result)