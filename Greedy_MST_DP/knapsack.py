
import base

cands, SIZE = base.load_knapsack()

# Optimal value: 9;   Optimal Knapsack: [4, 3]
# W = 6
testcase = [[3, 4], [2, 3], [5, 2], [4, 3]]


def knapsack(vwlist, W=SIZE):
    N = len(vwlist)
    mat = [[0 for _ in range(W+1)] for _ in range(N+1)]
    items = {}
    for x in range(1, W+1):
        for j in range(1, N+1):
            vj, wj = vwlist[j-1]
            mat[j][x] = mat[j-1][x]
            if wj <= x:
                include = mat[j-1][x-wj]+vj
                exclude = mat[j][x]
                mat[j][x] = max(include, exclude)
                # Keep track of the optimal knapsack items.
                if include >= exclude:
                    items[str(x)] = items.get(str(x-wj), []) + [j]
    print_mat(mat)
    return mat[N][W], items[str(W)]


def print_mat(mat):
    for row in mat:
        print(row, '\n')



if __name__ == '__main__':
    result, opt_knapsack = knapsack(testcase, 6)
    print('Optimal value:', result, '\nOptimal Knapsack:', opt_knapsack)