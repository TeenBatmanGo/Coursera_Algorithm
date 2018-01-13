
import base


# The implementation is based on python indexing (starting from 0)
def wis_dp(path):
    A = [0, path[0]]
    for i in range(2, len(path)+1):
        left = A[i-1]
        right = A[i-2] + path[i-1]
        if left < right:
            A.append(right)
        else:
            A.append(left)

    S = []
    j = len(A)-1
    while j >= 1:
        if A[j-1] >= A[j-2] + path[j-1]:
            j -= 1
        else:
            S.append(j-1)
            j -= 2
    cnt = 0
    for k in S:
        cnt += path[k]
    print('Max Sum:', cnt)
    return S




if __name__ == '__main__':
    # maxsum=4305, points=[1, 3, 5, 7]
    testcase = [1, 200, 20, 4000, 2, 5, 10, 100]

    mwis = base.load_mwis()
    result = wis_dp(mwis)

    output = []
    for t in test:
        if t-1 in result:
            output.append(str(1))
        else:
            output.append(str(0))
    print(''.join(output))