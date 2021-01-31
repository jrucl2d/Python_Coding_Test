from itertools import permutations
operatorChar = ['+', '-', '*', '/']

n = int(input())
numbers = list(map(int, input().split()))
operatorsInput = list(map(int, input().split()))
operators = []
for i in range(4):
    for inner in range(operatorsInput[i]):
        operators.append(operatorChar[i])

candidate = list(permutations(operators, len(operators)))

outerMax = -1e9
outerMin = 1e9
for innerCase in candidate:
    oneCase = []
    oneCase.append(numbers[0])
    for index in range(len(innerCase)):
        oneCase.append(innerCase[index])
        oneCase.append(numbers[index + 1])

    innerCalced = oneCase[0]  # 첫 번째 숫자로 초기화
    for i in range(1, len(oneCase), 2):
        operator = oneCase[i]
        innerNum = oneCase[i+1]
        if operator == '+':
            innerCalced += innerNum
        elif operator == '-':
            innerCalced -= innerNum
        elif operator == '*':
            innerCalced = int(innerCalced * innerNum)
        elif operator == '/':
            innerCalced = int(innerCalced / innerNum)
    outerMax = max(outerMax, innerCalced)
    outerMin = min(outerMin, innerCalced)

print(outerMax)
print(outerMin)
