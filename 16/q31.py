t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tmpArr = list(map(int, input().split()))

    arr = []
    j = 0
    for i in range(n):
        tmpInner = []
        for j in range(m):
            tmpInner.append(tmpArr[i*m + j])
        arr.append(tmpInner)

    for j in range(1, m):
        for i in range(n):
            theNum = arr[i][j]
            nextNum = -1e9
            if i - 1 >= 0:
                nextNum = max(nextNum, theNum + arr[i-1][j-1])
            nextNum = max(nextNum, theNum + arr[i][j-1])
            if i + 1 < n:
                nextNum = max(nextNum, theNum + arr[i+1][j-1])
            arr[i][j] = nextNum
    ans = -1e9
    for i in range(n):
        ans = max(ans, arr[i][m - 1])

    print(ans)
