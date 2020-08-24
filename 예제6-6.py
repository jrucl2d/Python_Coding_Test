arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 계수 정렬 : O(n+k) - 데이터 개수 n개, 최대 수 크기 k일 때. 공간 복잡도 역시 O(n+k)

count = [0] * (len(arr)+1)  # 최대 숫자가 9이므로 0 포함 10 크기의 빈 배열

for i in arr:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")
