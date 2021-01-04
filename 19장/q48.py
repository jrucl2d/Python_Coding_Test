# 칸 수, 상어 수, 냄새 유지 시간
n, m, k = map(int, input().split())

# 기본 방향 : 위, 아래, 왼, 오른
dx = [99, -1, 1, 0, 0]
dy = [99, 0, 0, -1, 1]

# 테이블
arr = [[0] for _ in range(n)]
smellarr = [[[0, 0]] * n for _ in range(n)]

# 상어 현재 방향
sdir = []

# 상어들의 위치
slocs = [-1234]

# 상어들의 방향 우선순위 -> 위, 아래, 왼, 오른
dirOrder = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    arr[_] = tmp

sdir = list(map(int, input().split()))

for i in range(m):
    tmp = []
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    dirOrder.append(tmp)


def get_possible_locs(sharkNum, x, y):
    blanks = []
    same = []
    for i in range(1, 5):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if smellarr[nx][ny] == [0, 0]:
                blanks.append((nx, ny))
            if smellarr[nx][ny][0] == sharkNum:
                same.append((nx, ny))
    return (blanks, same)


def dir_to_index(dirNum):
    return (dx[dirNum], dy[dirNum])


def can_go_loc(sharkNum, x, y):
    # 주위 빈 칸과 자기 냄새 칸 목록을 불러옴
    blanks, sames = get_possible_locs(sharkNum, x, y)

    # 우선순위 표를 참고하여 빈칸이 있으면 그 곳으로 이동
    now_shark_dir = sdir[sharkNum - 1]
    for next_dir in dirOrder[sharkNum - 1][now_shark_dir - 1]:
        nx, ny = dir_to_index(next_dir)
        nx, ny = nx + x, ny + y
        for blank in blanks:
            if blank[0] == nx and blank[1] == ny:
                sdir[sharkNum - 1] = next_dir
                return (nx, ny)

    # 빈칸이 없을 경우 우선순위 표를 참고하여 자기 냄새 칸이 있으면 그 곳으로 이동
    for next_dir in dirOrder[sharkNum - 1][now_shark_dir - 1]:
        nx, ny = dir_to_index(next_dir)
        nx, ny = nx + x, ny + y
        for same in sames:
            if same[0] == nx and same[1] == ny:
                sdir[sharkNum - 1] = next_dir
                return (nx, ny)


# 처음 상어 위치 처리
tmp = []
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            smellarr[i][j] = [arr[i][j], k]
            tmp.append((arr[i][j], [i, j]))


tmp.sort()
for i in tmp:
    slocs.append(i[1])

time = 0
while True:
    time += 1

    want_to_gos = []

    for sharkNum in range(1, m + 1):
        if slocs[sharkNum] == -1234:
            continue
        bx = slocs[sharkNum][0]
        by = slocs[sharkNum][1]
        nx, ny = can_go_loc(sharkNum, bx, by)
        want_to_gos.append((sharkNum, bx, by, nx, ny))

    # 냄새 배열 하나씩 줄이기
    for i in range(n):
        for j in range(n):
            if smellarr[i][j] != [0, 0]:
                smellarr[i][j] = [smellarr[i][j][0], smellarr[i][j][1] - 1]
                if smellarr[i][j][1] == -1 or smellarr[i][j][1] == 0:
                    smellarr[i][j] = [0, 0]

    for sharkNum, bx, by, nx, ny in want_to_gos:
        arr[bx][by] = 0  # 이전 위치는 없는 것으로

        if arr[nx][ny] != 0:  # 만약 이미 해당 위치에 상어가 있다면
            beforeNum = arr[nx][ny]
            beforeSmell = smellarr[nx][ny]
            if arr[nx][ny] > sharkNum:
                arr[nx][ny] = sharkNum
                slocs[arr[nx][ny]] = -1234
                smellarr[nx][ny] = [sharkNum, k]
            else:
                arr[nx][ny] = beforeNum
                slocs[sharkNum] = -1234
                smellarr[nx][ny] = beforeSmell
        else:
            arr[nx][ny] = sharkNum
            slocs[sharkNum] = [nx, ny]
            smellarr[nx][ny] = [sharkNum, k]
    count = 0
    for i in slocs:
        if i == -1234:
            count += 1
    if count == m:
        print(time)
        break
    if time > 1000:
        print(-1)
        break
