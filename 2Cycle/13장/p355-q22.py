from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def get_next(pos, board):
    next_pos = []
    pos = list(pos)
    a, b, c, d = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):
        na, nb, nc, nd = a + dx[i], b + dy[i], c + dx[i], d + dy[i]
        if board[na][nb] == 0 and board[nc][nd] == 0:
            next_pos.append({(na, nb), (nc, nd)})

    if a == c:  # p1 - p2
        for i in [-1, 1]:
            if board[a + i][b] == 0 and board[c + i][d] == 0:
                next_pos.append({(a, b), (a + i, b)})
                next_pos.append({(c, d), (c + i, d)})
    elif b == d:  # p1 / p2s
        for i in [-1, 1]:
            if board[a][b + i] == 0 and board[c][d + i] == 0:
                next_pos.append({(a, b), (a, b + i)})
                next_pos.append({(c, d), (c, d + i)})

    return next_pos


def solution(board):
    n = len(board)
    nboard = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            nboard[i + 1][j + 1] = board[i][j]
    q = deque()
    visited = []
    first = {(1, 1), (1, 2)}
    q.append((first, 0))
    visited.append(first)

    while q:
        now, cost = q.popleft()

        if (n, n) in now:
            return cost

        for next_pos in get_next(now, nboard):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
