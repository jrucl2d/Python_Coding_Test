n = int(input())
arr = []

for i in range(n):
    tmp = input().split()
    arr.append((tmp[0], int(tmp[1])))


def setting(data):
    return data[1]


arr = sorted(arr, key=setting)

for i in range(n):
    print(arr[i][0], end=" ")
