import heapq
MAX = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dijkstra(arr):
    q = []
    darr = [[MAX] * (len(arr)) for _ in range(len(arr))]  # 거리 테이블
    heapq.heappush(q, (arr[0][0], (0, 0)))  # 시작지점의 비용을 우선순위 큐에 추가
    darr[0][0] = arr[0][0]  # 시작 지점의 비용

    while q:
        dist, (a, b) = heapq.heappop(q)  # 현재 최단 거리

        # 이미 처리된 노드
        if darr[a][b] < dist:
            continue

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr):
                continue

            cost = arr[nx][ny] + dist
            if cost < darr[nx][ny]:
                darr[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

    return darr[len(arr) - 1][len(arr) - 1]


t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    arr = []
    for __ in range(n):
        arr.append(list(map(int, input().split())))
    ans.append(dijkstra(arr))

for i in ans:
    print(i)
