def remove_consecutive_duplicates(s):
    lst = []
    c = None
    for i in s.split(' '):
        if i != c:
            lst.append(i)
            c = i
    return ' '.join(lst)
    