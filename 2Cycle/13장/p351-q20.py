from itertools import combinations

n = int(input())
arr = []
stus = []
blanks = []
for i in range(n):
    arr.append(list(input().split()))
    for j in range(n):
        if arr[i][j] == 'S':
            stus.append((i, j))
        if arr[i][j] == 'X':
            blanks.append((i, j))


def check():
    for stu in stus:
        x = stu[0]
        y = stu[1]
        # left
        shield = False
        for i in range(x, -1, -1):
            if arr[i][y] == 'T':
                if shield:
                    break
                else:
                    return False
            elif arr[i][y] == 'O':
                shield = True
        # right
        shield = False
        for i in range(x, n):
            if arr[i][y] == 'T':
                if shield:
                    break
                else:
                    return False
            elif arr[i][y] == 'O':
                shield = True
        # down
        shield = False
        for i in range(y, -1, -1):
            if arr[x][i] == 'T':
                if shield:
                    break
                else:
                    return False
            elif arr[x][i] == 'O':
                shield = True
        # up
        shield = False
        for i in range(y, n):
            if arr[x][i] == 'T':
                if shield:
                    break
                else:
                    return False
            elif arr[x][i] == 'O':
                shield = True
    return True


yes = False
for comb in list(combinations(blanks, 3)):
    arr[comb[0][0]][comb[0][1]] = 'O'
    arr[comb[1][0]][comb[1][1]] = 'O'
    arr[comb[2][0]][comb[2][1]] = 'O'
    if check():
        yes = True
        break
    arr[comb[0][0]][comb[0][1]] = 'X'
    arr[comb[1][0]][comb[1][1]] = 'X'
    arr[comb[2][0]][comb[2][1]] = 'X'

if yes:
    print("YES")
else:
    print("NO")
