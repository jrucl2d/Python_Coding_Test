n = int(input())

ansCount = 0
# time = [0, 0, 0, 0, 0, 0]

# while time != [0, n + 1, 0, 0, 0, 0]:
#     if time[0] == 3 or time[1] == 3 or time[2] == 3 or time[3] == 3 or time[4] == 3 or time[5] == 3:
#         ansCount += 1

#     time[5] += 1
#     if time[5] == 10:
#         time[4] += 1
#         time[5] = 0
#     if time[4] == 6:
#         time[3] += 1
#         time[4] = 0
#     if time[3] == 10:
#         time[2] += 1
#         time[3] = 0
#     if time[2] == 6:
#         time[1] += 1
#         time[2] = 0

# 더 좋은 풀이 배열에서 사용되는 연산자 'in'을 사용
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                ansCount += 1
print(ansCount)
