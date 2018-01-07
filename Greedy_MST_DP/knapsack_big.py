
import base

cands, SIZE = base.load_knapsack(small=False)


# Since we don't need to reconstruct, we only need the previous row.
def knapsack(vwlist, W=SIZE):
    N = len(vwlist)
    mat = [[0 for _ in range(W+1)] for _ in range(2)]
    for j in range(1, N+1):
        vj, wj = vwlist[j - 1]
        for x in range(1, W+1):
            mat[1][x] = mat[0][x]
            if wj <= x:
                include = mat[0][x - wj] + vj
                exclude = mat[1][x]
                mat[1][x] = max(include, exclude)
        mat[0] = mat[1].copy()
    return mat[1][W]



if __name__ == '__main__':
    result = knapsack(cands)
    print(result)