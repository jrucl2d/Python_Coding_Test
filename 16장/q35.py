import math
n = int(input())

arr = [1]

i = 1
for i in range(1, n):
    theMin = 1e9
    for j in arr:
        if j * 2 not in arr:
            theMin = min(theMin, j * 2)
        elif j * 3 not in arr:
            theMin = min(theMin, j * 3)
        elif j * 5 not in arr:
            theMin = min(theMin, j * 5)
    arr.append(theMin)

print(arr[n - 1])
