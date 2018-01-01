

testcase1 = {'A': ('B', 'E'),
             'B': ('A', 'C', 'D', 'F'),
             'C': ('B', 'G', 'D'),
             'D': ('B', 'C', 'G'),
             'E': 'A',
             'F': ('G', 'B'),
             'G': ('C', 'D', 'F')}


testcase2 = {'A': ('B', 'C'),
             'B': 'D',
             'C': 'D',
             'D': ()}



def dfs_loop(graph):
    v = list(graph.keys())
    n = len(v)
    visited = dict(zip(v, [False]*n))
    for vi in v:
        if not visited[vi]:
            dfs(graph, vi, visited)


def dfs(graph, start, visited):
    visited[start] = True
    for w in graph[start]:
        print(start, w, visited[w])
        if not visited[w]:
            visited[w] = True
            print('After checking:', start, w)
            dfs(graph, w, visited)


if __name__ == '__main__':
    dfs_loop(testcase2)

