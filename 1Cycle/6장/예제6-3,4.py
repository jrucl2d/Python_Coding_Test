arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# quick 정렬 : 평균 O(nlogn). 최악 O(n^2). 거의 이미 정렬되어 있는 경우 효율이 안 좋다.


def quick(arr, start, end):
    if start >= end:  # 원소가 하나인 경우 리턴
        return
    pivot = start  # 시작점을 피벗으로 삼음
    left = start + 1
    right = end
    while left <= right:
        # 이 두 순서가 바뀌면 안 됨. left <= end로 먼저 검사 해야 함
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 right - 1의 위치와 pivot 위치 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:  # 그 이외에는 pivot 기준으로 다른 위치에 있는 left와 right을 교체
            arr[left], arr[right] = arr[right], arr[left]
    quick(arr, start, right - 1)
    quick(arr, right + 1, end)


quick(arr, 0, len(arr)-1)

print(arr)

# 파이썬의 특징을 살린 더 쉬운 quick sort. 그러나 시간 면에서는 조금 비효율적이다.


def quick2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 첫 요소를 피벗으로
    tail = arr[1:]  # 나머지 리스트
    left = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    return quick2(left) + [pivot] + quick2(right)


print(quick2(arr2))
