n=int(input())
a=list(map(int,input().split()))
a=sorted(a, reverse=True)
d=[]
while n>=2:
    d.append(a[1])
    a.remove(a[1])
    n-=1
print(sum(d))