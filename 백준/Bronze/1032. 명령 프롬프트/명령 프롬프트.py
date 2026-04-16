n = int(input())
arr = []
arr2 = []
r = []
for i in range(n):
    arr.append(list(input()))
for i in range(len(arr[0])):
    e = []
    for j in range(n):
        e.append(arr[j][i])
    arr2.append(''.join(e))
for i in arr2:
    if i[0]*n == i:
        r.append(i[0])
    else:
        r.append('?')
print(''.join(r))