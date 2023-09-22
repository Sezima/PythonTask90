
'Replace with alphabet position'

def alphabet_position(text):
    a = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    for i in text.lower():
        if i in a:
            lst.append(str(a.find(i)+1))
    return ' '.join(lst)