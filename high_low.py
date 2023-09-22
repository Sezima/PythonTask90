def high_and_low(numbers):
    lst = []
    for i in numbers.split(' '):
        lst.append(int(i))
    return f'{max(lst)} {min(lst)}'

high_and_low("54 46 -9")