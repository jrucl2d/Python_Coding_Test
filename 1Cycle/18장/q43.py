def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [i for i in range(n)]

edges = []

for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()  # 비용을 기준으로 오름차순 sort

ans = 0

for edge in edges:
    cost, a, b = edge
    ans += cost

    if find_parent(parent, a) != find_parent(parent, b):  # 사이클 발생하지 않으면
        union_parent(parent, a, b)
        ans -= cost

print(ans)
