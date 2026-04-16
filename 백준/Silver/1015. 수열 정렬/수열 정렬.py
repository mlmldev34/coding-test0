n=int(input())
a=list(map(int,input().split()))
b=list(sorted(a))
r=[]
for i in range(n):
    for j in range(n):
        if not(b.index(a[i])+j in r):
            r.append(b.index(a[i])+j)
            break
print(' '.join(list(map(str,r))))