def digital_root(n):
    x = str(n)
    r = 0
    if len(x) == 1:
        return int(x)
    else:
        while len(x) > 1:
            r = 0
    for i in range(len(x)):
        r = r + int(x[i])
        x = str(r)
    return r
