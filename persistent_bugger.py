import functools
def persistence(n):
    count = 0
    while n > 9:
        n = functools.reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        count += 1
    return count
