
import base

g = base.load_g(3)



def bellman_ford(graph, s):
    V = list(graph.keys())
    n = len(V)
    A = {v: 1e10 for v in V}
    A[s] = 0

    for i in range(n-1):
        for v in V:
            for neigh in graph[v]:
                if A[neigh] > A[v] + graph[v][neigh]:
                    A[neigh] = A[v] + graph[v][neigh]
    for v in V:
        for neigh in graph[v]:
            if A[neigh] > A[v] + graph[v][neigh]:
                print('############# Negative Circle ################')
                return None
    return A




def dijkstra(graph, start, vals):
    V = list(graph.keys())
    A = {(start, start): 0}
    included = [start]
    while len(included) < len(V):
        mindist, min_v = 1e10, start
        for v in included:
            for neigh in graph[v]:
                if neigh not in included:
                    dist = graph[v][neigh] + A[(start, v)]
                    if dist<mindist:
                        min_w = neigh
                        mindist = dist

        A[(start, min_w)] = mindist
        included.append(min_w)
    for ele in A:
        A[ele] = A[ele] - vals[ele[0]] + vals[ele[1]]
    return A




def johnson(graph):
    V = list(graph.keys())
    graph['S'] = {v: 0 for v in V}
    vals = bellman_ford(graph, 'S')
    if vals is None:
        return 'Null'
    del graph['S']
    for v in V:
        for neigh in graph[v]:
            graph[v][neigh] = graph[v][neigh] + vals[v] - vals[neigh]
    min_dist = 1e10
    for v in V:
        dists = dijkstra(graph, v, vals)
        if min(list(dists.values())) < min_dist:
            min_dist = min(list(dists.values()))
    return min_dist



if __name__ == '__main__':
    result = johnson(g)
    print(result)

