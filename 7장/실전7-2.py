import sys
n = int(input())
nArr = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
mArr = list(map(int, sys.stdin.readline().rstrip().split()))

# def binary(arr, target, left, right):
#     if left > right:
#         return None
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary(arr, target, mid+1, right)
#     else:
#         return binary(arr, target, left, mid - 1)
# nArr.sort()
# for i in mArr:
#     if binary(nArr, i, 0, n - 1) == None:
#         print("no", end=" ")
#     else:
#         print("yes", end=" ")

# 다른 풀이 : 계수 정렬의 아이디어를 사용. set을 이용한 풀이도 있음

maxNum = max(nArr) + 1
countArr = [0] * maxNum
for i in range(n):
    countArr[nArr[i]] = i
for i in mArr:
    if countArr[i] == 0:
        print("no", end=" ")
    else:
        print("yes", end=" ")