from itertools import combinations

n, m = map(int, input().split())
graph = []
modified = []
cells = []

for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    modified.append(arr[:])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cells.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(graph, x, y):
    graph[x][y] = 3
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 0:
            dfs(graph, nx, ny)


answer = 0

candidate = list(combinations(cells, 3))
for three in candidate:
    count = 0
    modified[three[0][0]][three[0][1]] = 1
    modified[three[1][0]][three[1][1]] = 1
    modified[three[2][0]][three[2][1]] = 1
    for i in range(n):
        for j in range(m):
            if modified[i][j] == 2:
                modified[i][j] = 0
                dfs(modified, i, j)
    for i in range(n):
        for j in range(m):
            if modified[i][j] == 0:
                count += 1

    for i in range(n):
        for j in range(m):
            modified[i][j] = graph[i][j]
    answer = max(answer, count)

print(answer)
