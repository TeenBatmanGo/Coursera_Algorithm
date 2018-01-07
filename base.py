
PATH = '/Users/wangchengming/Documents/Algorithms/Coursera/Coursera_Algorithm/data/'



def load_Integer_Array():
    with open(PATH + 'Integer_Array.txt', 'r') as f:
        arr = []
        for row in f.readlines():
            arr.append(str(int(row)))
    return arr


def load_QuickSort():
    with open(PATH + 'QuickSort.txt', 'r') as f:
        nums = []
        for row in f.readlines():
            nums.append(int(row))
    return nums


def load_adjacency_list():
    with open(PATH + 'kargerMinCut.txt', 'r') as f:
        adjcency_li = {}
        for row in f.readlines():
            elements = str.split(row, '\t')
            adjcency_li[elements[0]] = elements[1:-1]
    return adjcency_li


def load_scc():
    with open(PATH + 'SCC.txt', 'r') as f:
        adjcency_li = []
        for row in f.readlines():
            elements = str.split(row, ' ')[:-1]
            adjcency_li.append(elements)
    return adjcency_li


def load_dijkstradata():
    with open(PATH + 'dijkstraData.txt', 'r') as f:
        adjcency_dict = {}
        for row in f.readlines():
            elements = str.split(row, '\t')[:-1]
            adjcency_dict[elements[0]] = elements[1:]
    return adjcency_dict


def load_Median():
    with open(PATH + 'Median.txt', 'r') as f:
        medians = []
        for row in f.readlines():
            medians.append(int(row))
    return medians


def load_2sum():
    with open(PATH + '2sum.txt', 'r') as f:
        nums = []
        for row in f.readlines():
            nums.append(int(row))
    return nums


def load_jobs():
    with open(PATH + 'jobs.txt', 'r') as f:
        next(f)
        jobs = {}
        cnt = 1
        for row in f.readlines():
            row = row[:-1]
            elements = row.split(' ')
            jobs[str(cnt)] = [int(i) for i in elements]
            cnt += 1
    return jobs


def load_edges():
    with open(PATH + 'edges.txt', 'r') as f:
        next(f)
        edges = {}
        for row in f.readlines():
            row = row[:-1]
            elements = row.split(' ')
            edges[(elements[0], elements[1])] = int(elements[2])
    return edges


def load_clustering():
    with open(PATH + 'clustering1.txt', 'r') as f:
        next(f)
        clusters = {}
        for row in f.readlines():
            row = row[:-1]
            elements = row.split(' ')
            clusters[(elements[0], elements[1])] = int(elements[2])
    return clusters


def load_clustering_big():
    with open(PATH + 'clustering_big.txt', "r") as f:
        lines = f.readlines()
        seq = {}
        for i, line in enumerate(lines[1:]):
            bitseq = tuple(bool(int(x)) for x in line.split())
            seq[bitseq] = True
    return seq


def load_clustering_big_bruteforce():
    with open(PATH + 'clustering_big.txt', 'r') as f:
        next(f)
        clusters = {}
        for row in f.readlines():
            row = row[:-1]
            row = row.replace(' ', '')
            clusters[row] = True
    return clusters


def load_huffman():
    import heapq
    with open(PATH + 'huffman.txt', 'r') as f:
        next(f)
        weights = []
        lines = f.readlines()
        for i in range(len(lines)):
            row = lines[i][:-1]
            heapq.heappush(weights, int(row))
    return weights


def load_mwis():
    with open(PATH + 'mwis.txt', 'r') as f:
        next(f)
        mwis = []
        for row in f.readlines():
            row = row[:-1]
            mwis.append(int(row))
    return mwis


def load_knapsack(small=True):
    if small:
        name = 'knapsack1.txt'
        size = 10000
    else:
        name = 'knapsack_big.txt'
        size = 2000000
    with open(PATH + name, 'r') as f:
        next(f)
        lines = f.readlines()
        cands = []
        for i in range(len(lines)):
            row = lines[i][:-1].split(' ')
            cands.append([int(j) for j in row])
    return cands, size