n, m = map(int, input().split())
a, b, d = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr[a][b] = 1


def move():
    global a, b, d
    if d == 0:  # 북
        d = 3
        nb = b - 1
        if arr[a][nb] == 1:  # 왼쪽이 갈 수 없다면 false 리턴
            return False
        b = b - 1  # 갈 수 있다면 왼쪽으로 한 칸 전진 후 true 리턴
        arr[a][b] = 1
        return True
    elif d == 1:  # 동
        d = 0
        na = a - 1
        if arr[na][b] == 1:
            return False
        a = a-1
        arr[a][b] = 1
        return True
    elif d == 2:  # 남
        d = 1
        nb = b + 1
        if arr[a][nb] == 1:
            return False
        b = b+1
        arr[a][b] = 1
        return True
    else:  # 서
        d = 2
        na = a + 1
        if arr[na][b] == 1:
            return False
        a = a+1
        arr[a][b] = 1
        return True

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1


def goBack():
    global a, b, d
    if d == 0:
        b = b - 1
    elif d == 1:
        a -= 1
    elif d == 2:
        b += 1
    else:
        a += 1


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
        goBack()
        if arr[a][b] == 1:
            break
print(ansCnt)
