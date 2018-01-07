
import base

jobs = base.load_jobs()

testcase = {'1': [8, 50], '2': [74, 59],
            '3': [31, 73], '4': [45, 79],
            '5': [24, 10], '6': [41, 66]}



def key_diff(element):
    return element[0]-element[1], element[0]

def key_ratio(element):
    return element[0]/element[1], element[0]


def greedy(dicts, orderby='difference'):
    ordering = []
    for key in dicts.keys():
        val = dicts[key]
        ordering.append(val)
    if orderby == 'ratio':
        ordering.sort(key=key_ratio, reverse=True)
    elif orderby == 'difference':
        ordering.sort(key=key_diff, reverse=True)

    completion_time, L = 0, 0
    for element in ordering:
        w, l = element
        L += l
        completion_time += w*L
    return completion_time



if __name__ == '__main__':
    time = greedy(jobs, 'ratio')
    print(time)