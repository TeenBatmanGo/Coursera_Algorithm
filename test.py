
# For testing algorithms.

def invert(x):
    n = len(str(x))
    if n <= 1:
        return x
    return str(x)[-1]+invert(str(x)[:-1])




if __name__ == '__main__':
    a = 12
    print(invert(a))
