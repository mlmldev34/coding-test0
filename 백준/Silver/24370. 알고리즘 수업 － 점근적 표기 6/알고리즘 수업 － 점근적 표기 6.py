a2,a1,a0=map(int,input().split())
c1,c2=map(int, input().split())
n0=int(input())
t1=0
t2=0

if (a2-c1)==0:
    if a1<0:
        t1=0
    elif a1>0:
        if (-a0/a1 <= n0):
            t1=1
        else:
            t1=0
    else:
        if (a0>=0):
            t1=1
        else:
            t1=0
elif (a2-c1)>0:
    if (a1**2-4*a0*(a2-c1)>=0):
        x1=(-a1-(a1**2-4*a0*(a2-c1))**0.5)/(2*(a2-c1))
        x2=(-a1+(a1**2-4*a0*(a2-c1))**0.5)/(2*(a2-c1))
        if x1>x2:
            x1,x2=x2,x1
        if x1==x2:
            t1=1
        else:
            if(n0>=x2):
                t1=1
            else:
                t1=0
    else:
        t1=1
else:
    t1=0

if (a2-c2)==0:
    if a1<0:
        t2=0
    elif a1>0:
        if (-a0/a1 <= n0):
            t2=1
        else:
            t2=0
    else:
        if (a0<=0):
            t2=1
        else:
            t2=0
elif (a2-c2)<0:
    if (a1**2-4*a0*(a2-c2)>=0):
        x1=(-a1-(a1**2-4*a0*(a2-c2))**0.5)/(2*(a2-c2))
        x2=(-a1+(a1**2-4*a0*(a2-c2))**0.5)/(2*(a2-c2))
        if x1>x2:
            x1,x2=x2,x1
        if x1==x2:
            t2=1
        else:
            if(n0>=x2):
                t2=1
            else:
                t2=0
    else:
        t2=1
else:
    t2=0

print(int(t1 and t2))