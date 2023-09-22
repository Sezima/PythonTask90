'Draw stairs'
def draw_stairs(n):
    c = 0 
    s = ''
    while n > c:
        for i in range(n):
            s += ' '*i + 'I'
            c += 1
        if n > c:
            s += '\n'
    return s

