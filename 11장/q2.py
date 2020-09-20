s = input()

ans = int(s[0])
for i in range(len(s) - 1):
    if s[i] == '0' or s[i] == '1':
        ans += int(s[i + 1])
    else:
        ans *= int(s[i + 1])

print(ans)