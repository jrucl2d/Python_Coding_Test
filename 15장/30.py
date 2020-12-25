from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)] 
    rarr = [[] for _ in range(10001)] # 뒤집힌 문자
    for word in words: # '해당 문자의 길이' 행에 넣음
        arr[len(word)].append(word)
        rarr[len(word)].append(word[::-1])
    for i in range(10001): # 정렬 수행
        arr[i].sort()
        rarr[i].sort()
    for query in queries:
        res = 0
        if query[0] == '?': # query?? -> queryaa ~ queryzz 사이에 속하는 문자 개수를 구한다
            res = bisect_right(rarr[len(query)], query[::-1].replace('?', 'z')) - bisect_left(rarr[len(query)], query[::-1].replace('?', 'a'))
        else:
            res = bisect_right(arr[len(query)], query.replace('?', 'z')) - bisect_left(arr[len(query)], query.replace('?', 'a'))
        answer.append(res)
    return answer