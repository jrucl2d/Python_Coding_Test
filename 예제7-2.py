def binary(arr, target, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid + 1
    elif arr[mid] < target:
        return binary(arr, target, mid + 1, right)
    else:
        return binary(arr, target, left, mid - 1)

arr = [1,3,5,7,9,11,13,15,17,19]
target = 7
print(binary(arr, target, 0, len(arr) - 1))