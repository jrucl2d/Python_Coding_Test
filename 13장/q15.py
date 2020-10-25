from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n + 1)

answer = []


def bfs(graph, start, visited):
    depth = 0
    queue = deque([(start, depth)])
    visited[start] = True
    while queue:
        v, depth = queue.popleft()
        if depth == k:
            answer.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append((i, depth + 1))
                visited[i] = True


bfs(graph, x, visited)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for ans in answer:
        print(ans)
