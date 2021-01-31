import copy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

arr = [[] for _ in range(4)]
for _ in range(4):
    tmp = list(map(int, input().split()))
    for i in range(4):
        arr[_].append([tmp[2 * i], tmp[2 * i + 1]])


def find_pos(arr, index):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return (i, j)

    return None


ans = 0


def fish_move(arr, sx, sy):
    for num in range(1, 17):  # 1 ~ 16까지 순서대로 움직임
        position = find_pos(arr, num)
        if position != None:
            x, y = position[0], position[1]
            theDir = arr[x][y][1]
            for j in range(8):
                nx, ny = x + dx[theDir-1], y + dy[theDir-1]
                if nx >= 0 and ny >= 0 and nx < 4 and ny < 4:
                    if not (nx == sx and ny == sy):
                        arr[x][y][1] = theDir
                        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                        break
                theDir = (theDir + 1) % 8


def check_move(arr, sx, sy):
    positions = []
    direction = arr[sx][sy][1]
    for i in range(4):
        sx += dx[direction-1]
        sy += dy[direction-1]
        if 0 <= sx and sx < 4 and sy >= 0 and sy < 4 and arr[sx][sy][0] != -1:
            positions.append((sx, sy))
    return positions


def dfs(arr, sx, sy, total):
    global ans
    arr = copy.deepcopy(arr)

    total += arr[sx][sy][0]
    arr[sx][sy][0] = -1

    fish_move(arr, sx, sy)

    positions = check_move(arr, sx, sy)

    if len(positions) == 0:
        ans = max(ans, total)
        return
    for nx, ny in positions:
        dfs(arr, nx, ny, total)


dfs(arr, 0, 0, 0)
print(ans)
