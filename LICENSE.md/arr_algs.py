def min(arr):
    amin = arr[0]
    for i in arr:
        if i < amin:
            amin = i
    return amin

def avg(arr):
    s = 0
    for i in arr:
        s += i
    return s//len(arr)

arr1 = [10,8,12,0]
print(min(arr1))
print(avg(arr1))

