a2,a1,a0=map(int,input().split())
c=int(input())
n0=int(input())
t=0

if (a2-c)==0:
    if a1<0:
        t=0
    elif a1>0:
        if (-a0/a1 <= n0):
            t=1
        else:
            t=0
    else:
        if (a0>=0):
            t=1
        else:
            t=0
elif (a2-c)>0:
    if (a1**2-4*a0*(a2-c)>=0):
        x1=(-a1-(a1**2-4*a0*(a2-c))**0.5)/(2*(a2-c))
        x2=(-a1+(a1**2-4*a0*(a2-c))**0.5)/(2*(a2-c))
        if x1>x2:
            x1,x2=x2,x1
        if x1==x2:
            t=1
        else:
            if(n0>=x2):
                t=1
            else:
                t=0
    else:
        t=1
else:
    t=0

print(t)