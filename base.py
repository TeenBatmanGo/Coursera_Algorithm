
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
        adjcency_li = {}
        for row in f.readlines():
            elements = str.split(row, ' ')
            if str(elements[0]) in adjcency_li.keys():
                adjcency_li[str(elements[0])].append(elements[1])
            else:
                adjcency_li[str(elements[0])] = [elements[1]]
    return adjcency_li

