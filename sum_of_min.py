def sum_of_minimums(numbers):
    c = []
    for i in numbers:
        if min(i):
            c.append(min(i))
    return sum(c)

sum_of_minimums([[ 1, 2, 3, 4, 5 ], [ 5, 6, 7, 8, 9 ], [ 20, 21, 34, 56, 100 ]])