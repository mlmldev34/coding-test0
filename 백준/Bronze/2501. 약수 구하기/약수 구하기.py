n,k=map(int,input().split())
c=0
t=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        if c==k:
            print(i)
            t=1
            break
if t==0:
    print(0)