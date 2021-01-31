import itertools
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = list(map(int, input().split()))

ans = 0
for x in itertools.combinations(balls, 2):
    if x[0] != x[1]:
        ans += 1

print(ans)