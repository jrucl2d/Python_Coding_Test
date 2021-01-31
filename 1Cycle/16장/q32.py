n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = []

for inner in arr:
    tmp = []
    for num in inner:
        tmp.append(0)
    dp.append(tmp)
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(len(arr[i])):
        if j - 1 >= 0:
            dp[i][j] = max(dp[i-1][j-1] + arr[i][j], dp[i][j])
        if j < len(arr[i]) - 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + arr[i][j])

ans = 0
for i in dp[n - 1]:
    ans = max(ans, i)
print(ans)
