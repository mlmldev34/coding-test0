l,r,x=map(int,input().split())
a=[]
for i in range(l,r+1):
    a.append(i|x)
a=sorted(a)
r=0
if a != [i for i in range(0,len(a))]:
    if a[0]>0:
        r=0
    elif a[-1]>len(a)-1:
        b=[i for i in range(a[0],a[-1]+1)]
        for k in list(set(b)&set(a)):
            b.pop(k)
        r=sorted(b)[0]
else:
    r=a[-1]+1
print(r)