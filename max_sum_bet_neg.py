'max sum between two negatives'
def max_sum_between_two_negatives(arr: list) -> int:
    n: list = []
    intr: list = []
    my_sum: list = []
    for i in range(len(arr)):
        if arr[i] < 0:
            n.append(i)
        if len(n) < 2:
            return -1
    for k in range(len(n) - 1):
        intr.append(arr[n[k]:n[k + 1]])
    for j, k in enumerate(intr):
        my_sum.append(sum(intr[j][1:]))
        return max(my_sum) if max(my_sum) > 0 else 0
