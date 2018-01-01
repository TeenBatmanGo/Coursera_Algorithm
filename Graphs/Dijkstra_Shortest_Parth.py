
import base

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
        mindist, min_v = 1e8, start
        for v in included:
            neigh = get_neighbours(graph, v)
            for i in range(len(neigh)):
                if neigh[i] not in included:
                    dist = get_dist(graph, v, neigh[i]) + A[v]
                    if dist<mindist:
                        min_v = v
                        min_w = neigh[i]
                        mindist = dist

        B[min_w] = B[min_v] + [min_w]
        A[min_w] = mindist
        included.append(min_w)
        print('\nShortest Path to', min_w, 'is', B[min_w], '\nDistance is', A[min_w])

    return A




if __name__ == '__main__':
    result = dijkstra(testcase1, '1')
    print('\n', result, sep='')
    # result = dijkstra(adjacency_dict, '1')
    # temp = []
    # for i in [7,37,59,82,99,115,133,165,188,197]:
    #     temp.append(result[str(i)])
    # print('\n', temp, sep='')