n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

tour = list(map(int, input().split()))


def find_parent(parent, x):
    # 루트 노드가 아니면 루트 노드 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


parent = [0] * (n + 1)
for i in range(1, n + 1):  # 부모 배열을 자기자신을 루트로 초기화
    parent[i] = i

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:  # 길이 있다면 union
            union_parent(parent, i + 1, j + 1)

same = True
theParent = parent[tour[0]]

for i in range(1, m):
    if parent[i] != theParent:
        same = False

if same:
    print("YES")
else:
    print("NO")
