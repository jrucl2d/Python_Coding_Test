s = input()

strings = ''
numbers = 0
for i in s:
    if i.isdigit():
        numbers += int(i)
    else:
        strings += i
strings = ''.join(sorted(strings))
print(strings, end="")
if numbers != 0:
    print(numbers)