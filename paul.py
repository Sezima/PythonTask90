"Paul's Misery"
def paul(x):
    c = 0
    for i in x:
        if i == 'kata':
            c += 5
        elif i == 'Petes kata':
            c += 10
        elif i == 'life':
            c += 0
        else:
            c += 1
    if c < 40:
        return 'Super happy!'
    elif 70 > c >= 40:
        return 'Happy!'
    elif 70 <= c < 100:
        return 'Sad!'
    else:
        return 'Miserable!'