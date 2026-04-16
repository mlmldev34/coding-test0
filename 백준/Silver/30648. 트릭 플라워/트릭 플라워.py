a, b = map(int, input().split())
R = int(input())

x = a
y = b
t = 1
arr = []
arr.append([a, b])

while True:
    if x+1 + y+1 < R:
        x = x+1
        y = y+1
    else:
        x = x//2
        y = y//2
    if [x, y] in arr:
        break
    else:
        arr.append([x, y])
    t += 1
print(t)