from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

q = deque()


def BFS(index):
    q.append(index)
    visited[index] = True
    while q:
        index = q.popleft()
        print(index, end=" ")
        for i in graph[index]:
            if not visited[i]:
                q.append(i)
                visited[i] = True  # 스택을 사용하는 DFS와는 다르게 여기서 방문처리 해줘야 함


BFS(1)
