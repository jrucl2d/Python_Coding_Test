n = int(input())

k = list(map(int, input().split()))

dp = [0] * n
dp[0] = k[0]
dp[1] = max(k[0], k[1])

for i in range(2, n):
    # 두 경우가 존재. i-1을 털었으면 i를 못 털고, 안 털면 i를 털 수 있다.
    dp[i] = max(dp[i-1], dp[i-2] + k[i])

print(dp[n - 1])

# 4
# 1 3 1 5
