
import base
import numpy as np

adjacency_dict = base.load_dijkstradata()


testcase1 = {'1': ['2,1', '8,2'],
             '2': ['1,1', '3,1'],
             '3': ['2,1', '4,1'],
             '4': ['3,1', '5,1'],
             '5': ['4,1', '6,1'],
             '6': ['5,1', '7,1'],
             '7': ['6,1', '8,1'],
             '8': ['7,1', '1,2']}



def get_neighbours(graph, v):
    li = graph[v]
    return [i.split(',')[0] for i in li]

def get_dist(graph, v, w):
    li = graph[v]
    for i in li:
        num = i.split(',')
        if num[0] == w:
            return int(num[1])


def dijkstra(graph, start):
    A = {start: 0}
    B = {start: [start]}
    included = list(A.keys())
    while len(included) < len(list(graph.keys())):
        dist_li = []
        for v in included:
            neigh = get_neighbours(graph, v)

            if len(neigh)==0:
                continue

            dist_li_sub = []
            for i in range(len(neigh)):

                if neigh[i] in included:
                    dist_li_sub.append(1e8)
                    continue

                dist = get_dist(graph, v, neigh[i]) + A[v]
                dist_li_sub.append(dist)

            if len(dist_li_sub) == 0:
                continue

            ind = np.argmin(dist_li_sub)
            w = neigh[ind]
            dist_li.append((v, w, dist_li_sub[ind]))

        ind = np.argmin([i[2] for i in dist_li])
        v, w, dist = dist_li[ind]
        B[w] = B[v] + [w]
        A[w] = dist
        included.append(w)
        print('\nShortest Path to', w, 'is', B[w], '\nDistance is', A[w])

    return A




if __name__ == '__main__':
    result = dijkstra(testcase1, '1')
    print('\n', result)
    # result = dijkstra(adjacency_dict, '1')
    # temp = []
    # for i in [7,37,59,82,99,115,133,165,188,197]:
    #     temp.append(result[str(i)])
    # print('\n', temp)