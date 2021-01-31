position = input()
# ascii -> char : chr
# char -> ascii : ord
position = [ord(position[0]) - ord('a'), int(position[1]) - 1]

# 변하지 않는 값은 튜플로
possible = [(-2, -1), (-2, 1), (2, -1),
            (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
ans = 0
for i in range(8):
    nx = position[0] + possible[i][0]
    ny = position[1] + possible[i][1]
    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        continue
    ans += 1

print(ans)
