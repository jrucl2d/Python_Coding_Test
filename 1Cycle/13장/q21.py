from collections import deque

n, l, r = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
path = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j):
    global visited, path

    if visited[i][j]:
        return

    dq = deque()
    dq.append((i, j))

    while(dq):
        (a, b) = dq.popleft()
        path.append((a, b))
        visited[a][b] = True

        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if nx >= 0 and ny >= 0 and nx < n and ny < n and not visited[nx][ny]:
                if abs(graph[a][b] - graph[nx][ny]) >= l and abs(graph[a][b] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    dq.append((nx, ny))


ans = 0

while True:
    # 변수 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    path = []  # 하나의 연합
    outerPath = []  # 모든 연합들

    for i in range(n):
        for j in range(n):
            bfs(i, j)  # i, j부터 시작해서 연합을 구성
            if len(path) > 1:  # 연합이 구성되면 outerPath에 추가
                outerPath.append(path)
            path = []  # 현재의 연합 정보를 저장하는 path 변수 초기화
    if len(outerPath) == 0:  # outerPath가 0이면 더이상 연합이 존재하지 않음 -> 종료
        break
    for innerPath in outerPath:
        theSum = 0
        theNum = len(innerPath)
        for a in innerPath:
            theSum += graph[a[0]][a[1]]
        for a in innerPath:
            graph[a[0]][a[1]] = int(theSum / theNum)
    ans += 1

print(ans)
