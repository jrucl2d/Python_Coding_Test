# 시작점에서 k까지의 최단거리 + k에서 x까지의 최단거리를 구하면 됨
import heapq
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # a에서 b로 가는 길이 존재한다는 뜻
    graph[b].append(a)  # 양방향 가능

x, k = map(int, input().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist + 1 < distance[i]:
                distance[i] = dist + 1
                heapq.heappush(q, (distance[i], i))


dijkstra(1)
middleAns = distance[k]

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

dijkstra(k)
ans = middleAns + distance[x]

if (ans >= INF):
    print(-1)
else:
    print(ans)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5