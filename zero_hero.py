def no_boring_zeros(n):
    if n !=0 :
        if str(n).endswith('0'):
            return int(str(n).rstrip('0'))
        else:
            return n
    else:
        return 0
no_boring_zeros(0)     
