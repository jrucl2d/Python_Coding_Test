from itertools import combinations

# 4 6
# a t c i s w

moeum = ["a", "e", "i", "o", "u"]
letter = []
l, c = map(int, input().split())
letter = sorted(list(input().split()))

result = list(combinations(letter, l))

for innerArr in result:
    mCount = 0
    for value in innerArr:
        if value in moeum:
            mCount += 1
    if mCount >= 1 and (l - mCount) >= 2:
        print("".join(innerArr))

