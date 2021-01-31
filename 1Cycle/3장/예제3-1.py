money = [500, 100, 50, 10]
n = int(input())
ans = 0
for value in money:
    ans += int(n / value)
    n %= value
print(ans)
