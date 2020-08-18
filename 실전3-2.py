n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)

biggest = array[0]
nextBig = array[1]

rest = m % (k+1)
howMany = int(m / (k + 1))
ans = howMany * (biggest * k + nextBig) + rest * biggest
print(ans)
