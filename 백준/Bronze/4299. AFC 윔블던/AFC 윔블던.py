a,b=map(int,input().split())
if (a+b)%2==0:
    x=(a+b)//2
else:
    x=-1
if (a-b)%2==0:
    y=(a-b)//2
else:
    y=-1
if x==-1 or y==-1 or x<0 or y<0:
    print(-1)
else:
    if x>y:
        print(x,y)
    else:
        print(y,x)