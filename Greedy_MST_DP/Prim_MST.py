
import base

edges = base.load_edges()

# answer is 37
testcase = {('1', '2'): 4, ('2', '3'): 7,
            ('3', '4'): 7, ('4', '5'): 9,
            ('5', '6'): 10, ('6', '7'): 2,
            ('7', '8'): 1, ('8', '9'): 7,
            ('1', '8'): 8, ('2', '8'): 11,
            ('3', '9'): 2, ('3', '6'): 4,
            ('4', '6'): 14, ('7', '9'): 6}



def mst(tree):
    V = set([i[0] for i in tree.keys()]) | set([i[1] for i in tree.keys()])
    X = set('1')
    total_cost = 0
    while len(V) - len(X) > 0:
        new_v = None
        cost = 1e10
        for u in X:
            for v in (V-X):
                if (u, v) in tree.keys():
                    if tree[(u, v)] < cost:
                        cost = tree[(u, v)]
                        new_v = v
                elif (v, u) in tree.keys():
                    if tree[(v, u)] < cost:
                        cost = tree[(v, u)]
                        new_v = v
        if new_v:
            X.add(new_v)
            total_cost += cost
            print('############# Add', new_v, '     cost:', cost)
    return total_cost




if __name__ == '__main__':
    costs = mst(edges)
    print('\nTotal cost is', costs)
