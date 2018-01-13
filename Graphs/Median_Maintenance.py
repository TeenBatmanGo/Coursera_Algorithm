
import base
import heapq


def heap_median(li):
    H_low = []
    H_high = []
    H_min, H_max = 0, 0
    cnt = 0
    for element in li:
        if element <= H_max:
            heapq.heappush(H_low, -element)
        else:
            heapq.heappush(H_high, element)

        if len(H_low)-len(H_high) > 1:
            temp = heapq.heappop(H_low)
            heapq.heappush(H_high, -temp)
        elif len(H_high)-len(H_low) > 1:
            temp = heapq.heappop(H_high)
            heapq.heappush(H_low, -temp)

        if len(H_low) >= len(H_high):
            # print('\nCurrent element:', element, '    H_left:', H_low, '    H_right:', H_high)
            print('Median:', -H_low[0])
            cnt += -H_low[0]
        else:
            # print('\nCurrent element:', element, '    H_left:', H_low, '    H_right:', H_high)
            print('Median:', H_high[0])
            cnt += H_high[0]

        H_max = -H_low[0] if len(H_low) > 0 else 0
    return cnt % 10000



if __name__ == '__main__':
    nums = base.load_Median()
    testcase = [2, 5, 1, 3, 4, 10, 6]
    result = heap_median(nums)
    print(result)
