def hydrate(drink_string): 
    n = []
    for i in list(drink_string.split()):
        if i.isnumeric():
            n.append(int(i))
    if sum(n) == 1:
        return f'{sum(n)} glass of water'
    else:
        return f'{sum(n)} glasses of water'