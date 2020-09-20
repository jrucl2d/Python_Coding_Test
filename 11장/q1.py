n = int(input())
arr = list(map(int, input().split()))

# 내 풀이
# arr.sort(reverse=True)

# groupNum = 0
# index = 0
# while True:
#     groupNum += 1
#     index += arr[index]
#     if index >= len(arr):
#         break
# print(groupNum)

groupNum = 0
count = 0
for i in arr:
    count += 1  # 현재 인원을 그룹에 넣었을 때
    if count > i:  # 그룹의 총 수가 현재 인원의 공포도보다 크면(최소한의 인원으로 그룹을 꾸려야 하므로)
        groupNum += 1  # 새 그룹에 넣고
        count = 1  # 현재 인원을 시작으로 하는 새 그룹을 시작

print(groupNum)
