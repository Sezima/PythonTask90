'Consecutive items'
def consecutive(arr, a, b): 
    c = 0
    for i in range (len(arr) - 1):
        c += i
        if arr[i] == a :
            return arr[i + 1] == b
        elif arr[i] == b:
            return arr[i+1] == a
    return False
