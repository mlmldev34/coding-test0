from itertools import combinations as com

arr = list(map(int, input().split()))
s = sum(arr)
a = []
r = 0
x = 0

for i in list(com(arr, 2)):
    x = sum(i)
    a.append(abs(x*2-s))
print(min(a))