
testcase1 = {'dkpg':['multiarch_support', 'coreutils', 'tar', 'libbz2'],
            'coreutils':['libbz2', 'libselinux1'],
            'multiarch_support':[],
            'libselinux1':['multiarch_support'],
            'libbz2':['libselinux1'],
            'tar':[]}


testcase2 = {'A': ('B', 'E'),
             'B': ('C', 'D', 'F'),
             'C': ('G', 'D'),
             'D': ('B', 'C', 'G'),
             'E': (),
             'F': ('G', 'B')}



