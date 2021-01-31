from itertools import combinations

n, m = map(int, input().split())

city = []

for i in range(n):
    line = list(map(int, input().split()))
    city.append(line)

chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))


chickenRange = []  # 각 집들의 치킨집에 대한 치킨거리

for chick in chicken:  # 치킨집의 위치들
    x = chick[0]  # 현재 치킨집의 행
    y = chick[1]  # 현재 치킨집의 열
    ranges = []  # 해당 치킨 집에 대해 치킨 거리를 저장
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                ranges.append(abs(i - x) + abs(j - y))
    chickenRange.append(ranges)

chosenCandidate = []
for i in range(len(chicken)):  # 0~치킨집 개수
    chosenCandidate.append(i)

chosen = list(combinations(chosenCandidate, m))

answer = 1e9
for chosenChickenShop in chosen:
    outerAns = 0
    for ranges in range(len(chickenRange[0])):  # 현재 치킨집에 대한 각 집들의 치킨거리
        innerAns = 1e9  # 해당 집에서 각 치킨집들 중 더 짧은 거리를 고름
        for index in chosenChickenShop:
            innerAns = min(innerAns, chickenRange[index][ranges])
        outerAns += innerAns
    answer = min(answer, outerAns)

print(answer)
