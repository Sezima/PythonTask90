'your order please'
def order(sentence):
    lst = []
    for i in range(1,10):
        for j in sentence.split():
            if str(i) in j:
                lst.append(j)
    return " ".join(lst)