def show_sequence(n):
    c = 0
    s = ''
    if n == 0:
        return '0=0'
    elif n > 0 or n == 0:
        for i in range(n+1):
            c += i
            s += str(i) + '+'
            return s[:-1:] + ' = ' + str(c)
    else:
        return f'{n}<0'
show_sequence(-1)
