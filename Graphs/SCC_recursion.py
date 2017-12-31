
import sys
import base
import numpy as np
import threading
import heapq

sys.setrecursionlimit(1000000)

adjacency_li = base.load_scc()


testcase1 = [['1', '4'],
             ['2', '8'],
             ['8', '6'],
             ['4', '7'],
             ['5', '2'],
             ['6', '9'],
             ['7', '1'],
             ['3', '6'],
             ['8', '5'],
             ['9', '7'],
             ['9', '3']]


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


def find_all_vertices(target):
    set1 = set([row[0] for row in target])
    set2 = set([row[1] for row in target])
    return set1.union(set2)



t = 0
s = 0
def dfs_loop(graph, ordering, v, n, loop=1):
    visited = dict(zip(v, [False]*n))
    curr_time = {}
    num_li = [0]
    for vi in ordering:
        if not visited[vi]:
            if loop == 2:
                print(vi)
            curr_time, num = dfs(graph, vi, visited, curr_time, loop)
            num_li.append(num)
    if loop == 1:
        return curr_time
    elif loop == 2:
        sccs = [num_li[i]-num_li[i-1] for i in range(1, len(num_li))]
        if len(sccs) < 5:
            sccs.extend([0]*(5-len(sccs)))
        return heapq.nlargest(5, sccs)



def dfs(graph, start, visited, curr_time, loop=1):
    global t, s
    visited[start] = True
    graph[start] = graph.get(start, [])
    for w in graph[start]:
        if not visited[w]:
            visited[w] = True
            dfs(graph, w, visited, curr_time, loop)

    if loop == 2:
        s += 1
    t += 1
    curr_time[start] = t
    if loop == 1:
        print('Current time:', curr_time[start], '     Vertex:', start)
    return curr_time, s



def scc():
    v = find_all_vertices(adjacency_li)
    n = len(v)
    graph_reverse = to_dict(adjacency_li, True)
    graph = to_dict(adjacency_li)

    ordering = list(graph_reverse.keys())
    ordering = np.sort([int(i) for i in ordering])[::-1]
    ordering = [str(i) for i in ordering]
    finish_ordering = dfs_loop(graph_reverse, ordering, v, n)
    print('\nLoop #####################################\n')
    leaders = dfs_loop(graph, list(finish_ordering.keys())[::-1], v, n, 2)
    print(leaders)




if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=scc)
    thread.start()


