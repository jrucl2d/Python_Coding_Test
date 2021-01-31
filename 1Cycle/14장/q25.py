def solution(N, stages):
    stages.sort()
    answer = []
    totalNum = len(stages)
    
    pNum = 0 # 깬 사람 수
    for i in range(1, N + 1):
        if stages.count(i) == 0: # 깬 사람이 없다면
            answer.append((0, i))
        elif stages.count(i) != 0: # 깬 사람이 있다면
            answer.append(((stages.count(i) / (totalNum - pNum)), i))
            pNum += stages.count(i)
    
        
    answer.sort(key= lambda x : (-x[0], x[1]))
    result = []
    for i in answer:
        result.append(i[1])
    
    return result