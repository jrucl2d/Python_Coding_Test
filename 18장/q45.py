from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    before = [0]
    before.extend(list(map(int, input().split())))

    chaged = []
    c = int(input())
    for i in range(c):
        chaged.append(list(map(int, input().split())))

    indegree = [0] * (n + 1) # 진입 차수
    graph = [[] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph[before[j]].append(before[i]) # 이후의 팀들보다 현재 팀이 앞순위
            indegree[before[i]] += 1 # 진입 차수 증가
    
    for i in chaged:
        a = i[0]
        b = i[1]
        if b in graph[a]: # a에서 b로 가는 간선이 있다면
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            indegree[b] += 1
            indegree[a] -= 1

    result = []
    q = deque()

    # 진입 차수 0인 노드 넣기
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 사이클 생성시 -> IMPOSSIBLE
    # 가능하지만 여러 경우가 가능할 시 -> ?
    error = False

    for _ in range(n):
        if not q:
            print("IMPOSSIBLE")
            error = True
            break
        now = q.popleft()
        result.append(now) # 진입 차수가 0인 노드 삽입
        
        cnt = 0
        for i in graph[now]:
            indegree[i] -= 1 # 해당 원소가 진입하는 노드들의 진입차수 하나씩 감소
            if indegree[i] == 0:
                q.append(i) # 새로 진입차수 0이 된 노드 큐에 삽입
                cnt += 1
        if cnt > 1: # 경우의 수가 두 개 이상인 경우 ?
            print("?")
            error = True
            break

    if error:
        continue

    for i in range(n - 1, -1, -1):
        print(result[i], end=" ")
    print()
        