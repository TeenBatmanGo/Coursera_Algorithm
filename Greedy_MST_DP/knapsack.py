
import base

cands, SIZE = base.load_knapsack()

# Optimal value: 8;   Optimal Knapsack: [4, 3]
testcase = [[3, 4], [2, 3], [4, 2], [4, 3]]


def knapsack(vwlist, W=SIZE):
    N = len(vwlist)
    mat = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for x in range(1, W+1):
        for j in range(1, N+1):
            vj, wj = vwlist[j-1]
            mat[j][x] = mat[j-1][x]
            if wj <= x:
                include = mat[j-1][x-wj]+vj
                exclude = mat[j][x]
                mat[j][x] = max(include, exclude)
    print_mat(mat)

    # Top down approach to find the optimal knapsack.
    x, j = W, N
    optimal_knapsack = []
    while mat[j][x] != 0:
        vj, wj = vwlist[j-1]
        include = mat[j-1][x-wj]+vj
        exclude = mat[j][x]
        if include >= exclude:
            optimal_knapsack.append(j)
            x -= wj
        j -= 1
    return mat[N][W], optimal_knapsack


def print_mat(mat):
    for row in mat:
        print(row, '\n')



if __name__ == '__main__':
    result, opt_knapsack = knapsack(testcase, 6)
    print('Optimal value:', result, '\nOptimal Knapsack:', opt_knapsack)