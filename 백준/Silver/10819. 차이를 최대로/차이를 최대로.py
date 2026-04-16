import itertools as it
def minus(a):
    return abs(a[0]-a[1])

n=int(input())
a=list(map(int,input().split()))
a=list(sorted(a,reverse=True))
arr=[]
r=0
x=list(it.combinations(a,2))
for i in list(it.combinations(a,2)):
    arr.append([i[0], i[1]])
arr.sort(key=lambda x: minus(x), reverse=True)
brr={}
for i in a:
    brr.update({i:a.count(i)*2})
c=n-1
for i in arr:
    m=minus(i)
    if brr[i[0]]>0 and brr[i[1]]>0 and c>0:
        brr[i[0]]-=1
        brr[i[1]]-=1
        if list(brr.values()).count(0)>=n-1:
            brr[i[0]]+=1
            brr[i[1]]+=1
        else:
            r+=m
            c-=1
print(r)