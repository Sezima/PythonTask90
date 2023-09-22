def sum(*args):
    if not args:
        if type(args[0]) is int:
            return args
    x = 0
    for i in args:
        if type(i) is int:
            x += i
        elif str(i).isnumeric():
            x += int(i)
    return x
    