import copy
def rotate(key):
    n = len(key)
    res = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            res[c][n-1-r] = key[r][c]
    return res

def finding(key, Lock, newLen, m, n):
    for startI in range(newLen-m + 1):
        for startJ in range(newLen-m + 1):
            found = True
            tmp = copy.deepcopy(Lock)
            # 키를 Lock에 넣었을 때
            for i in range(startI, startI + m):
                for j in range(startJ, startJ + m):
                    tmp[i][j] += key[i - startI][j - startJ]
        
            for i in range(m - 1, m - 1 + n):
                for j in range(m - 1, m - 1 + n):
                    if tmp[i][j] != 1:
                        found = False
                        break
                if not found:
                    break
            
            if found:
                return True

def solution(key, lock):
    answer = True
    n = len(lock) # n * n
    m = len(key)
    newLen = n + m * 2 - 2
    Lock = [[0]* newLen for j in range(newLen)]
    
    for i in range(n):
        for j in range(n):
            Lock[i+m-1][j+m-1] = lock[i][j]
    
    for i in range(4):
        answer = finding(key, Lock, newLen, m, n)
        if answer:
            return True
        key = rotate(key) # 못 찾았으면 회전
    return False
