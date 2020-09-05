# 시작점에서 k까지의 최단거리 + k에서 x까지의 최단거리를 구하면 됨
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(n)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5