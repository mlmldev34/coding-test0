n,k=map(int,input().split())
a=list(map(int,input().split()))
x=0
y=0
for i in range(1,n):
    if len(a[0:n-i+1])>0:
        if a[-i]!=max(a[0:n-i+1]):
            t=a.index(max(a[0:n-i+1]))
            temp1=a[t]
            temp2=a[-i]
            a[-i],a[t]=a[t],a[-i]
            k-=1
            if k==0:
                x=temp1
                y=temp2
                break
if k>0:
    print(-1)
else:
    if x<y:
        print(x,y)
    else:
        print(y,x)