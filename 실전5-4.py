from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

q = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(i, j):
    q.append((i, j, 1))
    graph[i][j] = 0  # 시작 장소 간 것으로 표시
    while q:
        x, y, count = q.popleft()
        if x == n - 1 and y == m - 1:
            return count
        for index in range(4):
            nx = x + dx[index]
            ny = y + dy[index]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 1:
                q.append((nx, ny, count + 1))
                graph[nx][ny] = 0


print(BFS(0, 0))

# 5 6
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
