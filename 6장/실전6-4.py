n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

ans = 0
for i in range(n):
    if i < k:
        ans += b[i]
    else:
        ans += a[i]

print(ans)
