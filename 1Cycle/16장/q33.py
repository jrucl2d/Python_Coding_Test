n = int(input())

arr = []
for _ in range(n):
    a1, a2 = map(int, input().split())
    arr.append((a1, a2))

dp = [0 for _ in range(n)]

for i in range(n):
    cost = arr[i][1]
    length = arr[i][0]
    if i + length <= n:  # 현재의 dp를 계산
        dp[i] = max(dp[i], cost)
    for j in range(i + length, n):  # 현재 상담 이후의 날짜들의 dp를 계산
        if j + arr[j][0] <= n:
            dp[j] = max(dp[j], dp[i] + arr[j][1])

print(max(dp))
