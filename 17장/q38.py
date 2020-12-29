n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 2
    arr[b][a] = 1


for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            if arr[i][j] != 1 and arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1
            elif arr[i][j] != 2 and arr[i][k] == 2 and arr[k][j] == 2:
                arr[i][j] = 2
ans = 0
for i in arr:
    cnt = 0
    for inner in i:
        if inner == 0:
            cnt += 1
    if cnt == 2:
        ans += 1

print(ans)
