def solution(s):
    answer = int(1e9)
    length = len(s)
    for nowLen in range(1, length // 2 + 1):
        resultString = ''
        patternNum = 1  # 패턴의 중복 횟수
        nowString = s[0:nowLen]  # nowLen개의 문자로 이루어진 패턴의 후보
        startIndex = nowLen
        while startIndex < length and startIndex + nowLen <= length:
            if s[startIndex:startIndex + nowLen] == nowString:  # 패턴이 같으면 수를 늘림
                patternNum += 1
            else:  # 다르면 이전 패턴을 결과에 추가하는데, 1이면 숫자는 추가하지 않음
                if patternNum != 1:
                    resultString += str(patternNum)
                resultString += nowString
                patternNum = 1
                nowString = s[startIndex:startIndex + nowLen]
            startIndex += nowLen  # startIndex는 계속해서 현재 패턴의 길이만큼 증가
        if patternNum != 1:  # 패턴의 길이가 너무 길어 처리하지 못한 나머지 처리
            resultString += str(patternNum)
        resultString += nowString
        resultString += s[startIndex:]
        answer = min(answer, len(resultString))
    return answer


# 더 깔끔한 풀이
def solution2(s):
    length = len(s)
    answer = length
    for step in range(1, length // 2 + 1):
        resultString = ''
        count = 1  # 패턴의 중복 횟수
        nowString = s[0:step]  # nowLen개의 문자로 이루어진 패턴의 후보
        for j in range(step, length,
                       step):  # step씩 뛰어넘으며 step부터 시작해서 length까지 반복
            # 같은 문자열이면
            if nowString == s[j:j + step]:
                count += 1
            # 다른 문자열이면
            else:
                resultString += (str(count) +
                                 nowString) if count >= 2 else nowString
                nowString = s[j:j + step]
                count = 1
        # 남은 문자열 처리
        resultString += (str(count) + nowString) if count >= 2 else nowString
        answer = min(answer, len(resultString))
    return answer


print(solution("abcabcabcabcdededededede"))
