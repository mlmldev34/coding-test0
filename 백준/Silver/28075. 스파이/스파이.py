import itertools as it

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr+=list(map(int,input().split()))
r=0
t=0
brr=list(it.product(list(range(6)), repeat=n))
for i in brr:
    t=0
    prev=-1
    for j in list(i):
        if prev!=-1:
            if prev==j or prev+3==j or prev-3==j:
                t+=arr[j]//2
            else:
                t+=arr[j]
        else:
            t+=arr[j]
        prev=j
    if t>=m:
        r+=1

print(r)