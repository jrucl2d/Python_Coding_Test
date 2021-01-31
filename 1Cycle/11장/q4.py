import itertools
n = int(input())

arr = list(map(int, input().split()))
arr.sort()
# maxNum = sum(arr)

# ans = 1
# for maybeMin in range(1, maxNum):
#     found = False
#     for iterNum in range(1, n + 1):
#         for x in itertools.combinations(arr, iterNum):
#             if sum(x) == maybeMin:
#                 found = True
#                 ans += 1

#                 break
#         if found:
#             break
#     if maybeMin == ans:
#         print(ans)
#         break

target = 1
for x in arr:
    # 이미 1~target전 까지는 다 만들 수 있다. 따라서 x가 target보다 작다면 x + 1~target전 의 한 수 = target이므로 만들 수 있다.
    # 그러나 x가 target보다 크다면 만들 수 없다.
    if target < x:
        break
    target += x
print(target)

# 5
# 3 2 1 1 9