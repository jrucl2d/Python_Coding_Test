from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

theLeft = bisect_left(arr, x)
if theLeft == n:
    print(-1)
else:
    theRight = bisect_right(arr, x)
    print(theRight - theLeft)
