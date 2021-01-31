EMPTY = 0
APPLE = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def nextPos(x, y, dir):
    return (x + dx[dir], y + dy[dir])


def changeDir(dir, rotate):
    if rotate == 'D':
        return (dir + 1) % 4
    else:
        return (dir - 1) % 4


n = int(input())  # 보드의 크기
board = [[EMPTY] * (n+1) for _ in range(n+1)]

k = int(input())  # 사과의 개수
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = APPLE

move = []
l = int(input())
for _ in range(l):
    a, b = input().split()
    move.append((a, b))

snake = [(1, 1)]
direction = 0

time = 0
while(True):
    time += 1
    slen = len(snake)
    # 게임 오버 조건
    x, y = nextPos(snake[slen - 1][0], snake[slen - 1][1], direction)
    if x <= 0 or y <= 0 or x >= n + 1 or y >= n + 1:  # 벽에 부딛힘
        break
    elif (x, y) in snake:  # 자신의 몸에 부딛힘
        break

    # 방향 전환이 이루어져야 할 시
    for mov in move:
        if int(mov[0]) == time:
            direction = changeDir(direction, mov[1])

    # 사과가 있었으면
    if board[x][y] == APPLE:
        snake.append((x, y))
        board[x][y] = EMPTY
    else:  # 빈 칸이었으면
        snake.append((x, y))
        snake = snake[1:]

print(time)
