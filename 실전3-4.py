n, k = map(int, input().split())

# count = 0
# while n != 1:
#     if n % k == 0:
#         n = int(n / k)
#     else:
#         n -= 1
#     count += 1
# print(count)

count = 0
while True:
    # 일일이 1씩 빼주는 부분을 간결하게
    ones = n - (n // k) * k  # k로 나누기 위해서 빼줘야 하는 1의 개수
    n -= ones
    count += ones
    if n < k:
        break
    # 나누기 한 번 해주기
    count += 1
    n //= k

# 마지막으로 나머지 빼줘서 1 만들기
count += (n-1)
print(count)
