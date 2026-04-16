n=int(input())
a=sorted(list(map(int,input().split())))
k=-1
for i in range(a[0],a[-1]+1):
    if i not in a:
        k=i
        a.append(k)
        break
a=sorted(a)
if k!=-1:
    a=a[:a.index(k)]
l=[1]
for i in set(a):
    l.append(l[-1]*a.count(i))
if a[0]!=1:
    print(0)
else:
    print(sum(l)-1)