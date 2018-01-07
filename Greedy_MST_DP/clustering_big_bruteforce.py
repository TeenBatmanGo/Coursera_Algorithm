
import base

clusters = base.load_clustering_big_bruteforce()

# answer is 2
testcase = {'00001': True,
            '00010': True,
            '00100': True,
            '01111': True,
            '11111': True}



# Every cluster has a leader, when clusters merge together, the leader of the smaller cluster
# will point to the leader of the bigger one. Other elements stay the same.

class Cluster():
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



def mst_clustering(data):
    keys = list(data.keys())
    cls = Cluster(keys)
    # Use brute force bit shifting to find spacing = 1 or 2 vertices.
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            bit_i, bit_j = keys[i], keys[j]
            num_i, num_j = eval('0b'+str(bit_i)), eval('0b'+str(bit_j))
            diff = num_i ^ num_j
            cnt = 0
            while diff:
                diff = diff & (diff-1)
                cnt += 1
                if cnt > 2:
                    break
            if cnt != 3:
                cls.union(bit_i, bit_j)
    return cls.num_clusters



if __name__ == '__main__':
    import time
    start = time.time()
    result = mst_clustering(clusters)
    end = time.time()
    print('Number of Clusters:', result, '\nTime spent:', end-start)