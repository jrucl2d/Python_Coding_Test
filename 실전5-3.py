n, m = map(int, input().split())
graph = []
visited = [[False]*m for i in range(n)]  # 본 그래프가 문자열이라서 부득이하게 배열 하나 더 생성

# 북 동 서 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(i, j):
    visited[i][j] = True
    for index in range(4):
        nx = i + dx[index]
        ny = j + dy[index]
        if nx < n and ny < m and nx >= 0 and ny >= 0 and not visited[nx][ny]:
            DFS(nx, ny)


for i in range(n):
    tmp = input()
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == '1':
            visited[i][j] = True

ansCount = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            ansCount += 1
            DFS(i, j)
print(ansCount)


# 4 5
# 00110
# 00011
# 11111
# 00000

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
