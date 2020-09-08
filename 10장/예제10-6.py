from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)  # 진입 차수

# 각 노드에 연결된 간선 정보를 저장(연결 리스트)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # b의 진입 차수 하나 증가
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    # 처음에 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 하나 빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:  # 새롭게 진입차수가 0이 되면 큐에 삽입
                q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()
