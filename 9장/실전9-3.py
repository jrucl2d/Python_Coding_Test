import sys
import heapq
INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n+1)


for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    graph[i].append((j, k))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))


dijkstra(c)

count = 0
maxAns = 0
for i in range(1, n+1):
    if distance[i] >= INF:
        continue
    maxAns = max(maxAns, distance[i])
    count += 1


print(count - 1, maxAns)  # 시작점은 제외해야 함
