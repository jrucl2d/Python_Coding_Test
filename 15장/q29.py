n, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

between = arr[n - 1] - arr[0]  # 사이 최대거리 초기값
left = 1
right = between

while left <= right:
    mid = (right + left) // 2
    nextPoint = arr[0]  # 다음 위치
    count = 1  # 설치 개수
    for i in range(1, n):
        if arr[i] - nextPoint >= mid:
            nextPoint = arr[i]
            count += 1
    if count < c:
        right = mid - 1
    else:  # 더 큰 값에서도 가능할 수 있다.
        between = mid  # 현재까지의 최대값
        left = mid + 1

print(between)
