import base


adjcency_li = base.load_adjacency_list()


def contraction(adj_li, p1, p2):
    # contract p1 and p2 vertices into p1, with p1 element removed.
    p2_val = [val for val in adj_li[p2] if val != p1]
    adj_li[p1] += p2_val
    # remove p2 vertex
    adj_li.pop(p2, None)
    # replace p2 element in adj_li with p1.
    for key in adj_li.keys():
        if key==p1:
            adj_li[key] = [val for val in adj_li[key] if val != p2]
        else:
            adj_li[key] = [val if val != p2 else p1 for val in adj_li[key]]
    return adj_li


def karger(adj_li):
    from numpy.random import choice
#     np.random.seed(4)
    while len(adj_li)>2:
        keys = list(adj_li.keys())
        p1 = choice(keys)
        p2 = choice(adj_li[p1])
        adj_li = contraction(adj_li, p1, p2)
    return len(adj_li[list(adj_li.keys())[0]])



if __name__ == '__main__':
    from copy import deepcopy
    min_num = 1e10
    for i in range(100):
        adjcency_list = deepcopy(adjcency_li)
        num = karger(adjcency_list)
        if num < min_num:
            min_num = num
        if i%20 == 0:
            print('Iteration:', i, '         Current Min Num Cuts:', min_num)
    print('\n############# Minimum Cuts:', min_num, '#############')