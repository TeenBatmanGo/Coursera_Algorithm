
import base
import math
import numpy as np


def preprocess(clauses):

    """
    Key idea is to remove elements which have only one representation.
    i.e. 8 has only positive value.
    This means their boolean value is fixed.
    Clauses that contain at least one of these elements can be viewed as trivially satisfied.

    """

    prev_len = 0
    # Loop until no changes in the number of clauses.
    while prev_len - len(clauses) != 0:
        prev_len = len(clauses)
        pos, neg = set(), set()
        for row in clauses:
            for i in [0, 1]:
                if row[i] < 0:
                    neg.add(-row[i])
                else:
                    pos.add(row[i])
        diff = pos.symmetric_difference(neg)

        new_clauses = []
        for c in clauses:
            if len(set([abs(i) for i in c]).intersection(diff)) > 0:
                continue
            new_clauses.append(c)
        clauses = new_clauses

    print('The number of clauses can be reduced to', len(clauses))
    return clauses



def two_sat(clauses):
    N = len(clauses)
    clauses = preprocess(clauses)
    n = len(clauses)
    np.random.seed(1)
    for k in range(int(math.log2(n))):
        # initially assign boolean values to all clauses.
        # but only need to check for the nontrivial ones.
        assignment = [bool(np.random.choice([0, 1])) for _ in range(1, N+1)]
        for l in range(2*n**2):
            if check_sat(assignment, clauses):
                return 1
    return 0



def check_sat(assignment, clauses):
    for row in clauses:
        satisfy_left = assignment[row[0]] if row[0]>0 else not assignment[-row[0]]
        satisfy_right = assignment[row[1]] if row[1]>0 else not assignment[-row[1]]

        # ~(A v B) is equivalent as (~A ^ ~B)
        if not satisfy_left and not satisfy_right:
            flip = np.random.choice([0, 1])
            if flip == 0:
                assignment[abs(row[0])] = not assignment[abs(row[0])]
            elif flip == 1:
                assignment[abs(row[1])] = not assignment[abs(row[1])]
            return False

    return True




if __name__ == '__main__':
    NUM = 1
    target = base.load_2sat(NUM)
    result = two_sat(target)
    print('Satisfiable or not:', result)
