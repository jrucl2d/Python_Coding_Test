n = int(input())

arr = list(map(int, input().split()))
left = 0
right = n - 1

ans = -1

while left <= right:
    mid = (right + left) // 2
    if arr[mid] == mid:
        ans = mid
        break
    elif arr[mid] < mid:
        left = mid + 1
    else:
        right = mid - 1

print(ans)
