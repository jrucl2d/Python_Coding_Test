# find 연산
def find_parent(parent, x):
    # 루트 노드가 아니면 루트 노드 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    else:
        return x


# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:  # 더 큰 수가 작은 수를 가리키도록
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

# union 연산을 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

print('부모 테이블 출력: ', end=" ")
for i in range(1, v + 1):
    print(parent[i], end=" ")