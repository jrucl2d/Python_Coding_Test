n, m = map(int, input().split())
a, b, d = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr[a][b] = 1  # 첫 위치는 방문 처리

# 순서대로 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move():
    global a, b, d
    na = a + dx[d]
    nb = b + dy[d]
    d = 3 if d - 1 == -1 else d - 1
    if arr[na][nb] == 1:  # 왼 쪽이 갈 수 없다면 false를 리턴
        return False
    # 갈 수 있다면 한 칸 전진하고 true 리턴
    a = na
    b = nb
    arr[a][b] = 1
    return True


ansCnt = 1
while True:
    canGoNext = False
    for i in range(4):
        canGoNext = move()
        # print(a, b, d)
        if canGoNext:
            ansCnt += 1
            break
    if not canGoNext:
        a -= dx[d]  # 뒤로 이동
        b -= dy[d]
        if arr[a][b] == 1:
            break
print(ansCnt)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
