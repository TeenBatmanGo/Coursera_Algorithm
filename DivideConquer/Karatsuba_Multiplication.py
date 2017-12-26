
def Karatsuba(x, y):
    assert x.__class__ == str and y.__class__ == str, 'inputs must be strings.'
    n_x, n_y = len(x), len(y)
    n = max(n_x, n_y)

    if n < 2:
        return int(x) * int(y)

    if n_x != n or n_y != n:
        padding_x = '0' * (n - n_x)
        padding_y = '0' * (n - n_y)
        x = padding_x + x
        y = padding_y + y
    assert len(x) == len(y), 'x and y must have equal length.'

    mid = n // 2
    x_a, x_b = x[:mid], x[mid:]
    y_c, y_d = y[:mid], y[mid:]

    ac = Karatsuba(x_a, y_c)
    bd = Karatsuba(x_b, y_d)
    abcd = Karatsuba(str(int(x_a) + int(x_b)), str(int(y_c) + int(y_d)))
    ad_bc = abcd - ac - bd

    result = 10 ** (2 * (n - mid)) * ac + 10 ** (n - mid) * ad_bc + bd
    return result


if __name__ == '__main__':
    x = '315'
    y = '3248'
    result = Karatsuba(x, y)
    print(result, '\n', int(x) * int(y), sep='')