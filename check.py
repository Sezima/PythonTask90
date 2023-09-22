'check_exam'
def check_exam(arr1,arr2):
    c = 0
    for i in range(0,4):
        if arr1[i] == arr2[i]:
            c += 4
        elif arr2[i] == "":
            c += 0
        else: 
            c -= 1
    return c if c >= 0 else 0