
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