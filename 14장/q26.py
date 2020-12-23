import heapq

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

ans = 0
while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    ans += a + b
    heapq.heappush(arr, a + b)
print(ans)
