import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미. 10억

# 노드의 개수, 간선의 개수를 입력 받음
n, m = map(int, input().split())

# 시작 노드 번호를 입력받음
start = int(input())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())  # a에서 b로 가는 비용이 c라는 뜻
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드에 대해서 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):  # 현재 꺼낸 노드가 이미 처리되었다면 무시
            continue
        for i in graph[now]:  # 현재 위치에서 i[0]으로 가는데 드는 비용 i[1]
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 출력부
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
