arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 삽입 정렬 : O(n^2), 거의 정렬이 완료되어 있는 경우에는 O(n). 퀵 정렬보다 빠름


def sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:  # 순서에 맞게 되는 순간 멈춘다
                break


sort(arr)
print(arr)
