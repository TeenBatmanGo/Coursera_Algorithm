
import base
import heapq
import numpy as np


weights_heap = base.load_huffman()

# min_length=3, max_length=6
testcase = []
vals = [895, 121, 188, 953, 378, 849, 153, 579, 144, 727, 589, 301, 442, 327, 930]
for val in vals:
    heapq.heappush(testcase, val)



def huffman(weights):
    n = len(weights)
    original_weights = list(weights)
    depth = 0
    tree = []

    # Construct a tree which always chooses to split/merge on the left node.
    # Note that the leftmost path must be the longest path.
    # frop bottom to top, follow the leftmost path to compute maximum code length.
    while len(weights) > 1:
        temp1 = heapq.heappop(weights)
        temp2 = heapq.heappop(weights)
        if len(weights) == n-2:
            temp_sum = temp1
        if temp_sum in [temp1, temp2]:
            depth += 1
            temp_sum = temp1+temp2
        heapq.heappush(weights, temp1+temp2)
        tree.extend([temp1, temp2])

    # from top to bottom, find the nearest key to the root, take log2 to compute minimum code length.
    for i in range(len(tree)):
        if tree[::-1][i] in original_weights:
            min_code_len = np.log2(i+1).__trunc__()
            break
    return depth, min_code_len



if __name__ == '__main__':
    max_depth, min_depth = huffman(weights_heap)
    print('Maximum code length is', max_depth, '\nMinimum code length is', min_depth)

