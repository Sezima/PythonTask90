'descending order'
def descending_order(num):
    s = list(str(num))
    k = (sorted(s)[::-1])
    return int(''.join(k))

