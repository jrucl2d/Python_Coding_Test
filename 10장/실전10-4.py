from collections import deque
import copy  # 단순히 대입 연산을 하면 값 변경에 오류 발생 가능성 있음. deepcopy() 메소드 활용.

v = int(input())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:  # 1부터 끝까지
        indegree[i] += 1
        graph[x].append(i)  # 먼저 들어야 하는 강의 x의 후속 강의가 지금 강의 i


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:  # now에 연계된 후속 강의 i 중에서
            # 선수과목의 강의 시간이 현재 강의 시간보다 더 길면 현재 강의시간은 그것보다 늦어짐
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v + 1):
        print(result[i])


topology_sort()

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1