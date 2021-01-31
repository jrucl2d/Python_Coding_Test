import sys
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


# 방문하지 않은 노드 중 가장 작은 값을 찾음
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:  # 연결된 노드들에 대해서 처음 거리 설정
        distance[j[0]] = j[1]

    # 시작 노드 제외한 n-1개 노드에 대해서 반복
    for i in range(n - 1):
        now = get_smallest_node()  # 현재 가장 짧은 노드 찾음
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 또 확인
        for j in graph[now]:
            cost = distance[now] + j[1]  # 확인하는 값은 현재노드까지의 거리 + 다음 노드까지의 거리
            if cost < distance[j[0]]:
                distance[j[0]] = cost


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
