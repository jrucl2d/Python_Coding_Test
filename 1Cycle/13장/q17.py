from collections import deque

n, k = map(int, input().split())

graph = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

s, x, y = map(int, input().split())
x -= 1
y -= 1

germsInit = []  # 여기에 세균 초기 위치가 들어감
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            germsInit.append((graph[i][j], i, j))

germsInit.sort()
germs = deque(germsInit)  # 세균의 초기 위치가 오름차순으로 들어감

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

time = 0
while time != s:
    time += 1
    innerQueue = deque()
    while(germs):
        innerQueue.append(germs.popleft())
    while innerQueue:
        (germ, i, j) = innerQueue.popleft()
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            # print("nx와 ny는 ", nx, ny)
            if nx >= 0 and nx < n and ny >= 0 and ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = germ
                germs.append((germ, nx, ny))

print(graph[x][y])
