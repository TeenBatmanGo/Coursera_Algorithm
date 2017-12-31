
# answer is 6, 3, 2, 1, 0
testcase2 = [['1', '2'],
             ['2', '3'],
             ['2', '4'],
             ['2', '5'],
             ['3', '6'],
             ['4', '5'],
             ['4', '7'],
             ['5', '2'],
             ['5', '6'],
             ['5', '7'],
             ['6', '3'],
             ['6', '8'],
             ['7', '8'],
             ['7', '10'],
             ['8', '7'],
             ['9', '7'],
             ['10', '9'],
             ['10', '11'],
             ['11', '12'],
             ['12', '10']]


import numpy as np
import base
import sys
import os
import threading
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

sys.setrecursionlimit(1000000)


adjacency_li = base.load_scc()


def sort_strings(x):
    x = np.sort([int(i) for i in x])[::-1]
    x = [str(i) for i in x]
    return x


def to_dict(li, reverse=False):
    if reverse:
        li = [row[::-1] for row in li]
    dicts = {}
    for row in li:
        if str(row[0]) in dicts.keys():
            dicts[str(row[0])].append(row[1])
        else:
            dicts[str(row[0])] = [row[1]]
    return dicts



def dfs(graph, start, visited, fini_time, components):
    visited.add(start)
    stack = [start, start]
    while len(stack) > 0:
        target = stack.pop()
        if target not in stack:
            fini_time['time'] += 1
            fini_time[target] = fini_time['time']
        graph[target] = graph.get(target, [])
        for neigh in graph[target]:
            if neigh not in visited:
                stack.append(neigh)
                stack.append(neigh)
                visited.add(neigh)
        components.add(target)


def kosaraju(target):
    graph = to_dict(target)
    graph_reverse = to_dict(target, True)
    v = set(list(graph.keys())).union(set(list(graph_reverse.keys())))
    v = sort_strings(v)
    visited = set()
    components = set()
    fini_time = {'time': 0}
    for vi in v:
        if vi not in visited:
            dfs(graph_reverse, vi, visited, fini_time, components)

    v = list(fini_time.keys())[1:]
    v = sort_strings(v)
    visited = set()
    print('\nSecond Loop ##########################################\n')
    sccs = []
    for vi in v:
        components = set()
        if vi not in visited:
            dfs(graph, vi, visited, fini_time, components)
            sccs.append(components)
    sccs_len = [len(scc) for scc in sccs]
    if len(sccs_len) < 5:
        sccs_len.extend([0]*(5-len(sccs_len)))
    return np.sort(sccs_len)[::-1][:5]



if __name__ == '__main__':
    result = kosaraju(adjacency_li)
    print(result)