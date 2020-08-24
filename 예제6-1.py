arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택정렬 : O(n^2)


def sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


sort(arr)
print(arr)
