
"pandemia"
def infected(s):
    lst = s.split("X")
    tot = 0
    inf = 0
    for c in lst:
        tot += len(c)
        if "1" in c:
            c = c.replace("0", "1")
            inf += c.count("1")
    return 100 * inf / tot if inf > 0 else 0