
import base
import numpy as np
import matplotlib.pyplot as plt


# Recursively find all the 2^n subsets of {1, ..., n}
def all_subsets(items):
    if len(items) == 0:
        return [[]]
    first = items[0]
    rest = items[1:]
    subsets = []
    for partial_subset in all_subsets(rest):
        subsets.append(partial_subset)
        extend_subset = [first] + partial_subset
        subsets.append(extend_subset)
    return subsets

def compute_dist(data, i, j):
    datai, dataj = data[i], data[j]
    return np.sqrt((datai[0]-dataj[0])**2 + (datai[1]-dataj[1])**2)


# Dynamic programming approach.
def tsp(data):
    items = list(data.keys())
    n = len(items)
    subsets = all_subsets(items)
    subsets_tuple = [tuple(sub) for sub in subsets]
    A = {1: dict(zip(subsets_tuple, [1e10]*2**n))}
    A[1][tuple([1])] = 0
    for l in range(2, n+1):
        A[l] = {}

    prev = {}
    for m in range(2, n+1):
        for s in subsets:
            if 1 in s and len(s)==m:
                for j in s:
                    if j == 1:
                        continue
                    min_val = 1e10
                    for k in s:
                        if k == j:
                            continue
                        s_ = s.copy()
                        s_.pop(s_.index(j))
                        val = A[k][tuple(s_)] + compute_dist(data, j, k)
                        if val < min_val:
                            pp = k
                            min_val = val
                    A[j][tuple(s)] = min_val
                    prev[(j, tuple(s))] = pp

    # final hop of tour
    min_val = 1e10
    for j in range(2, n+1):
        val = A[j][tuple(items)] + compute_dist(data, j, 1)
        if val < min_val:
            final = j
            min_val = val

    # get the path
    path = [final, 1]
    for p in range(n-1):
        for sub in A[path[0]]:
            if path[0] not in list(sub):
                continue
            if len(sub) == n-p and prev[(path[0], sub)] not in path:
                path = [prev[(path[0], sub)]] + path

    return min_val, [1] + path




if __name__ == '__main__':
    # answer: 12.36
    testcase = {1: (0, 2.05), 2: (3.414213562373095, 3.4642135623730947),
                3: (0.5857864376269049, 0.6357864376269047), 4: (0.5857864376269049, 3.4642135623730947),
                5: (2, 0), 6: (4.05, 2.05),
                7: (2, 4.10), 8: (3.414213562373095, 0.6357864376269047)}


    # Due to observation from the scatter plot, this dataset can be divided into
    # two parts so that they can both be computed fast.
    left, right = base.load_tsp_half()

    # scatter plot. We can split according to edge (12, 13)
    N = len(left) + len(right) - 2
    labels = ['{0}'.format(i) for i in range(1, N+1)]
    coordsX = [left[coord][0] for coord in left]
    coordsY = [left[coord][1] for coord in left]
    coordsX.extend([right[coord][0] for coord in right if coord not in [1, 2]])
    coordsY.extend([right[coord][1] for coord in right if coord not in [1, 2]])

    plt.scatter(coordsX, coordsY, s=4)
    for label, x, y in zip(labels, coordsX, coordsY):
        plt.annotate(label, xy=(x, y))
    plt.show()

    # To combine two parts together, we need to subtract the common edge (12, 13)
    min_weight_left, min_path_left = tsp(left)
    min_weight_right, min_path_right = tsp(right)
    final_weight = min_weight_right + min_weight_left - 2*compute_dist(left, 12, 13)

    print('Left path:', min_path_left)
    print('Right path:', [i+11 for i in min_path_right])
    print('minimum weight left:', min_weight_left, '\nminimum weight right:', min_weight_right)
    print('Final minimum weight:', int(final_weight))
