from itertools import combinations

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

bins = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            bins.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(a, b, narr):
    stack = []
    stack.append((a, b))
    while len(stack) != 0:
        a, b = stack.pop()
        narr[a][b] = 2
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if narr[nx][ny] == 0:
                    stack.append((nx, ny))
    return narr


def check(narr):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if narr[i][j] == 0:
                cnt += 1
    return cnt


def copying(arr):
    narr = []
    for i in arr:
        narr.append(i[:])
    return narr


ans = 0
for poss in list(combinations(bins, 3)):
    narr = copying(arr)
    narr[poss[0][0]][poss[0][1]] = 1
    narr[poss[1][0]][poss[1][1]] = 1
    narr[poss[2][0]][poss[2][1]] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                narr = dfs(i, j, narr)
    inner_res = check(narr)
    ans = max(ans, inner_res)

print(ans)
