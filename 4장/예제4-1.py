n = int(input())
move = list(input().split())

start = [1, 1]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveType = ['L', 'R', 'U', 'D']

for direction in move:
    # if direction == 'L':
    #     nextX = start[0]
    #     nextY = start[1] - 1
    # elif direction == 'R':
    #     nextX = start[0]
    #     nextY = start[1] + 1
    # elif direction == 'U':
    #     nextX = start[0] - 1
    #     nextY = start[1]
    # elif direction == 'D':
    #     nextX = start[0] + 1
    #     nextY = start[1]
    for i in range(4):
        if moveType[i] == direction:
            nextX = start[0] + dx[i]
            nextY = start[1] + dy[i]
    if nextX < 1 or nextX > n or nextY < 1 or nextY > n:
        continue
    start = [nextX, nextY]
print(nextX, nextY)
