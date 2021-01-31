n, m = map(int, input().split())
arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# ans = 0
# for innerArr in arr:
#     myMin = 10001
#     for value in innerArr:
#         myMin = min(myMin, value)
#     ans = max(ans, myMin)

ans = 0
for _ in range(n):
    data = list(map(int, input().split()))
    tmp = min(data)  # 여기서 한 번에 구할 수 있다.
    ans = max(ans, tmp)

print(ans)
