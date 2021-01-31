# 소수 구하기
import math
m, n = map(int, input().split())

prime = [True for _ in range(1000001)]
prime[1] = False  # 1은 소수가 아님


def getPrimeNum(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i] == True:  # 소수라면 해당 수로 나눠지는 모든 수를 삭제
            j = 2  # i를 제외한 i의 배수를 삭제
            while i * j <= n:
                prime[i*j] = False
                j += 1


getPrimeNum(n)
for i in range(m, n + 1):
    if prime[i]:
        print(i)
