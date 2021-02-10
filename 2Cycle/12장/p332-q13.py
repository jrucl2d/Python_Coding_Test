from itertools import combinations
n, m = map(int, input().split())
chicks = []
homes = []
arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chicks.append((i, j))

nchicks = combinations(chicks, m)

ans = int(1e9)
for oneNchick in nchicks:
    inner_sum = 0
    for i in range(len(homes)):
        hx, hy = homes[i]
        # hx, hy 집에서 각 치킨집과의 거리 중 최소를 구함
        inner_min = int(1e9)
        for cpos in oneNchick:
            x, y = cpos
            inner_min = min(inner_min, abs(x - hx) + abs(y - hy))
        inner_sum += inner_min
    ans = min(ans, inner_sum)
print(ans)
