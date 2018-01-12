
import base
import math


def compute_dist(data, i, j):
    datai, dataj = data[i], data[j]
    return (datai[0]-dataj[0])**2 + (datai[1]-dataj[1])**2


# This is a heuristic approach which is just an approximation to the real solution.
def tsp(data):
    V = list(data.keys())
    n = len(V)
    visited = {}
    for v in V:
        visited[v] = False
    visited[V[0]] = True

    min_path_len = 0
    min_path = [V[0]]
    for i in range(n-1):
        min_dist = 1e10
        for u in V:
            if visited[u]:
                continue
            dist = compute_dist(data, u, min_path[-1])
            if dist < min_dist:
                min_dist = dist
                u_ = u
        min_path.append(u_)
        min_path_len += math.sqrt(min_dist)
        visited[u_] = True
    min_path_len += math.sqrt(compute_dist(data, min_path[0], min_path[-1]))
    return min_path_len


if __name__ == '__main__':
    dataset = base.load_nn()
    path_len = tsp(dataset)
    print(int(path_len)//1)

