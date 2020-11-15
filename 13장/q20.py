from itertools import combinations

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().split()))

maybe = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            maybe.append((i, j))


def isYes(graph, i, j):
    global n

    # 우측
    shield = 0
    for a in range(j, n):
        if graph[i][a] == 'O':
            shield += 1
        elif graph[i][a] == 'T':
            shield -= 1
            if shield < 0:
                return False
    # 좌측
    shield = 0
    for a in range(j, 0, -1):
        if graph[i][a] == 'O':
            shield += 1
        elif graph[i][a] == 'T':
            shield -= 1
            if shield < 0:
                return False

    # 상측
    shield = 0
    for a in range(i, n):
        if graph[a][j] == 'O':
            shield += 1
        elif graph[a][j] == 'T':
            shield -= 1
            if shield < 0:
                return False

    # 하측
    shield = 0
    for a in range(i, 0, -1):
        if graph[a][j] == 'O':
            shield += 1
        elif graph[a][j] == 'T':
            shield -= 1
            if shield < 0:
                return False

    return True


candidate = list(combinations(maybe, 3))

ans = True
for oneCase in candidate:
    ans = True
    for inner in oneCase:
        graph[inner[0]][inner[1]] = 'O'

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'S':
                if not isYes(graph, i, j):
                    ans = False
    if ans:
        break

    for inner in oneCase:
        graph[inner[0]][inner[1]] = 'X'

if ans:
    print("YES")
else:
    print("NO")
