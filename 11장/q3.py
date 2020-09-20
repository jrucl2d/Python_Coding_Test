s = input()

zeros = s.split('1')
ones = s.split('0')

first = 0
for i in zeros:
    if i != '':
        first += 1

second = 0
for i in ones:
    if i != '':
        second += 1
print(min(first, second))