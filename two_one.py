def longest(a1, a2):
    return "".join(sorted([i for i in set(a1 + a2)]))
    