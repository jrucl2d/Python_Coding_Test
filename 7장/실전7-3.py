import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
maxInt = max(arr)
ans = 0

# 이런 유형의 문제는 반복문으로 풀면 더 간단하다. 

def binary(arr, target, left, right):
    global ans
    if left > right:
        return None
    mid = (left + right) // 2
    tmpAns = 0
    for i in arr:
        tmpAns += ((i - mid) if (i - mid) > 0 else 0)  

    if target <= tmpAns:
        ans = max(ans, mid)
        return binary(arr, target, mid + 1, right)
    else:
        return binary(arr, target, left,mid - 1)

binary(arr, m, 0, maxInt)
print(ans)

    
# 4 6 
# 19 15 10 17