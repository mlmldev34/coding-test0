n = int(input())
a = input()
r = 0
i = 0
for _ in range(n):
    if i+4<=n:
        if a[i:i+4] == 'pPAp':
            r+=1
            i+=3
    i += 1
print(r)