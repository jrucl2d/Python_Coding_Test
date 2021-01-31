n, m = map(int, input().split())
money = []
dp = [987654321] * 10001
for i in range(n):
    tmp = int(input())
    money.append(tmp)
    dp[tmp] = 1
dp[0] = 0

for i in range(m + 1):
    for j in money:
        if i - j > 0:
            dp[i] = min(dp[i], dp[i - j] + 1)


if dp[m] == 987654321:
    print(-1)
else:
    print(dp[m])
