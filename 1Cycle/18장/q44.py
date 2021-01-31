n = int(input())
tmp = []
x = []
y = []
z = []
for _ in range(n):
    a, b, c = map(int, input().split())
    x.append((a, _))
    y.append((b, _))
    z.append((c, _))

x.sort()
y.sort()
z.sort()

edges = []

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i+1][1]))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n)]

edges.sort()

ans = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않으면
        union_parent(parent, a, b)
        ans += cost
print(ans)