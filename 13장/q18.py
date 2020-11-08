def balancedWhere(p):
    leftCount = 0  # 왼쪽 괄호
    for i in range(len(p)):
        if p[i] == '(':
            leftCount += 1
        else:
            leftCount -= 1
        if leftCount == 0:
            return i


def isRight(p):
    leftCount = 0  # 왼쪽 괄호
    for inner in p:
        if inner == '(':
            leftCount += 1
        else:
            if leftCount == 0:  # 쌍이 맞지 않는 경우
                return False
            leftCount -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balancedWhere(p)  # u와 v의 경계를 찾음
    u = p[:index + 1]
    v = p[index + 1:]
    if isRight(u):  # u가 올바르면 v에 대해 재귀적으로 수행
        answer = u + solution(v)
    else:
        answer = '('  # 4.1 빈 문자열에 (를 이어 붙임
        answer += solution(v)  # 4.2 v에 대해 1단계부터 재귀적으로 수행한 결과를 이어붙임
        answer += ')'  # 4.3 )를 다시 붙임
        u = list(u[1:-1])  # 4.4 u의 처음과 끝 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
