
import base

clusters = base.load_clustering()

testcase = {('1', '2'): 8.25,
            ('1', '3'): 11.18,
            ('1', '4'): 12.53,
            ('1', '5'): 10,
            ('1', '6'): 8,
            ('2', '3'): 3,
            ('2', '4'): 5,
            ('2', '5'): 4,
            ('2', '6'): 10,
            ('3', '4'): 4,
            ('3', '5'): 5,
            ('3', '6'): 12.53,
            ('4', '5'): 3,
            ('4', '6'): 11.18,
            ('5', '6'): 8.25}



def kruskal(data, k):
    V = set([i[0] for i in data.keys()]) | set([i[1] for i in data.keys()])
    cluster_num = len(V)
    sorted_data = sorted(data.items(), key=lambda d: d[1])
    sorted_edges = [elements[:2] for elements in sorted_data]
    E = set()
    for edge in sorted_edges:
        if not check_circles(E, edge):
            E.add(edge)
            cluster_num -= 1
        # To compute max spacing, a simple trick is to find k-1 clusters.
        # The edge which adds to the clusters will have the maximum spacing.
        if cluster_num < k:
            print('MST:', E)
            print(edge)
            break
    return None



def check_circles(edge_set, new_edge):
    v1 = [i[0][0] for i in edge_set]
    v2 = [i[0][1] for i in edge_set]
    V = v1 + v2
    graph = {}
    for i in range(len(v1)):
        graph[v1[i]] = graph.get(v1[i], []) + [v2[i]]
        graph[v2[i]] = graph.get(v2[i], []) + [v1[i]]
    if new_edge[0][0] not in graph.keys() or new_edge[0][1] not in graph.keys():
        return False
    return bfs(graph, start=new_edge[0][0], end=new_edge[0][1])



def bfs(graph, start, end):
    v = list(graph.keys())
    n = len(v)
    visited = dict(zip(v, [False]*n))
    L = {}
    for i in range(n):
        L[str(i)] = []
    L['0'] = [start]
    visited[start] = True
    for i in range(n):
        Li = L[str(i)]
        if end in Li:
            return True
        if not Li:
            break
        while Li:
            target = Li.pop(0)
            for k in graph[target]:
                if not visited[k]:
                    visited[k] = True
                    L[str(i+1)].append(k)
    return False



if __name__ == '__main__':
    kruskal(clusters, 4)

