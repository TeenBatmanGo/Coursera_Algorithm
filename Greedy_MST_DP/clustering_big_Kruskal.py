
import base


class Cluster():

    """
    Every cluster has a leader, when clusters merge together, the leader of the smaller cluster
    will point to the leader of the bigger one. Other elements stay the same.

    """

    def __init__(self, keys):
        self.size = {i:1 for i in keys}
        self.leader = {i:i for i in keys}
        self.num_clusters = len(keys)

    # Iteratively find the real leader of the cluster.
    def find(self, p):
        while p != self.leader[p]:
            self.leader[p] = self.leader[self.leader[p]]
            p = self.leader[p]
        return p

    def union(self, p, q):
        leader_p, leader_q = self.find(p), self.find(q)
        if leader_p == leader_q:
            return None
        if self.size[leader_p] < self.size[leader_q]:
            r1, r2 = leader_p, leader_q
        else:
            r1, r2 = leader_q, leader_p
        self.leader[r1] = r2
        self.size[r1] += self.size[r2]
        self.size[r2] = self.size[r1]
        self.reduceCluster()

    def reduceCluster(self):
        self.num_clusters -= 1

    def getCluster(self):
        return self.num_clusters



def mst_clustering(data, bits=24):
    keys = list(data.keys())
    cls = Cluster(keys)

    for k in keys:
        bitseq = list(k)
        diff_by_1 = set()
        for i in range(bits):
            neighbour = tuple(bitseq[:i] + [not bitseq[i]] + bitseq[i+1:])
            if neighbour in data:
                cls.union(k, neighbour)
            diff_by_1.add(neighbour)

        diff_by_2 = set()
        for j in range(bits):
            for d in diff_by_1:
                diff = list(d)
                neighbour = tuple(diff[:j] + [not diff[j]] + diff[j+1:])
                if neighbour in data:
                    cls.union(k, neighbour)
                diff_by_2.add(neighbour)

    return cls.num_clusters




if __name__ == '__main__':
    # answer is 2
    testcase = {(False, False, False, False, True): True,
                (False, False, False, True, False): True,
                (False, False, True, False, False): True,
                (False, True, True, True, True): True,
                (True, True, True, True, True): True}

    clusters = base.load_clustering_big()
    import time
    start = time.time()
    result = mst_clustering(clusters, 24)
    end = time.time()
    print('Number of Clusters:', result, '\nTime spent:', end-start)
    # Time spent: 223.72 seconds

