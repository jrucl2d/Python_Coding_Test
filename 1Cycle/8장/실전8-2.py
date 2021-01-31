x = int(input())

# dp = [30000] * 30001
# dp[x] = 0

# while True:
#     if x == 1:
#         break
#     if dp[x] == 30000:
#         continue
#     if x % 5 == 0:
#         dp[x // 5] = min(dp[x // 5], dp[x] + 1)
#     if x % 3 == 0:
#         dp[x // 3] = min(dp[x // 3], dp[x] + 1)
#     if x % 2 == 0:
#         dp[x // 2] = min(dp[x // 2], dp[x] + 1)
#     dp[x - 1] = min(dp[x - 1], dp[x] + 1)
#     x -= 1
# print(dp[1])

dp = [0] * 30001

for i in range(2, x + 1):
    dp[i] = dp[i-1] + 1
    if i % 5 == 0:
        dp[i] = min(dp[i // 5] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

print(dp[x])
