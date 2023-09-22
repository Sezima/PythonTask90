def xo(s):
    x, o = 0, 0
    for i in s:
        if i == 'x' or i == 'X':
            x += 1
        elif i == 'o' or i == 'O':
            o += 1
        if x == o:
            s = True
        else: 
            s = False
    return s