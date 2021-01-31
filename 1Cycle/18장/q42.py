g = int(input())
p = int(input())

airplane = []

for _ in range(p):
    airplane.append(int(input()))


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


parent = [i for i in range(g + 1)]

ans = 0
for inner in airplane:
    now = find_parent(parent, inner)
    if now == 0:
        break
    union_parent(parent, now, now - 1)
    ans += 1
print(ans)
