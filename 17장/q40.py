import heapq

n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]


def dijkstra(arr):
    global n
    q = []
    distance = [int(1e9) for _ in range(n + 1)]
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in range(n + 1):
            if arr[now][i] == 1:
                cost = arr[now][i] + dist

                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))
    return distance


for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

result = dijkstra(arr)

ans1 = 0
ans2 = -int(1e9)
ans3 = 0
for i in range(len(result) - 1, 0, -1):
    if ans2 <= result[i]:
        ans2 = result[i]
        ans1 = i
        ans3 += 1

print(ans1, ans2, ans3)
