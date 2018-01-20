
import heapq as hp

def heap_sort(x):
    heap = []
    for xi in x:
        hp.heappush(heap, xi)
    output = []
    while heap:
        minimum = hp.heappop(heap)
        output.append(minimum)
    return output


if __name__ == '__main__':
    testcase = [3, 6, 2, 4, 1, 1, 3, 2, 5, 8, 2]
    result = heap_sort(testcase)
    print(result)