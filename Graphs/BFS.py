
testcase = {'A': ('B', 'E'),
             'B': ('C', 'A', 'F'),
             'C': ('G', 'D', 'B'),
             'D': ('E', 'C', 'G'),
             'E': ('D', 'A'),
             'F': ('G', 'B'),
             'G': ('C', 'D', 'F')}


def bfs(graph, start):
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
        if Li:
            print('L', i, ': ', Li, sep='')
        else:
            break
        while Li:
            target = Li.pop(0)
            for k in graph[target]:
                if not visited[k]:
                    visited[k] = True
                    L[str(i+1)].append(k)
    return [v[i] for i in range(n) if visited[v[i]]]



if __name__ == '__main__':
    result = bfs(testcase, 'A')
    print(result)


