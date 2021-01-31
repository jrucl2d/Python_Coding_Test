def find_team(parent, x):
    if parent[x] != x:
        parent[x] = find_team(parent, parent[x])
    return parent[x]


def union_team(parent, a, b):
    a = find_team(parent, a)
    b = find_team(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 1:
        if find_team(parent, a) == find_team(parent, b):
            print("YES")
        else:
            print("NO")
    else:
        union_team(parent, a, b)

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1