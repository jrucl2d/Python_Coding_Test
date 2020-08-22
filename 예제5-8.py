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
    visited[index] = True
    print(index, " 방문")
    for i in graph[index]:
        if not visited[i]:
            DFS(i)


DFS(1)
