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


def DFS(index):
    visited[index] = True  # 원래 for문 안에서 방문 처리를 해야 하지만 바로 재귀로 오므로 여기서 해도 됨
    print(index, " 방문")
    for i in graph[index]:
        if not visited[i]:
            DFS(i)


DFS(1)
