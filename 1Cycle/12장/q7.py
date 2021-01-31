n = input()
mid = int(len(n) / 2)
left = n[0:mid]
right = n[mid:]

leftNum = 0
for i in left:
    leftNum += int(i)
rightNum = 0
for i in right:
    rightNum += int(i)
if leftNum == rightNum:
    print("LUCKY")
else:
    print("READY")