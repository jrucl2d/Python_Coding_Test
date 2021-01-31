from collections import deque
INF = int(1e9)

n = int(input())

px, py = 0, 0
theSize = 2
arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            px = i
            py = j
            arr[px][py] = 0  # 없는 것 처리

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


# 모든 위치의 최단 거리를 계산
def bfs():
    dist = [[-1] * n for _ in range(n)]  # 이동 못 하면 -1

    q = deque([(px, py)])  # 시작 위치
    dist[px][py] = 0  # 거리는 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if dist[nx][ny] == -1 and arr[nx][ny] <= theSize:
                    dist[nx][ny] = dist[x][y] + 1  # 한 칸 이동
                    q.append((nx, ny))
    return dist


def find_fish(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and arr[i][j] >= 1 and arr[i][j] < theSize:  # 도달 가능하고 먹을 수 있는 물고기
                if dist[i][j] < min_dist:  # <으로 처리해서 가장 i, j가 작은 것을 고르기
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist  # 물고기 위치와 최단 거리를 리턴


ans = 0
count = 0

while True:
    res = find_fish(bfs())  # 거리 계산한 상태로 먹을 물고기 위치와 거리를 리턴받음
    if res == None:
        print(ans)  # 더이상 먹지 못함
        break
    else:
        px, py = res[0], res[1]  # 현재 위치 갱신
        ans += res[2]  # 이동 거리 추가

        arr[px][py] = 0
        count += 1

        if count >= theSize:
            theSize += 1
            count = 0
