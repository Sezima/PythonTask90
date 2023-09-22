"Cat and mouse - easy"
def cat_mouse(x):
    ms = x.find('m')
    ct = x.find('C')
    if ms > ct:
        if ms - ct <= 4:
            return 'Caught!'
        else:
            return 'Escaped!'
    else:
        if ct - ms <= 4:
            return 'Caught!'
        else:
            return 'Escaped!'