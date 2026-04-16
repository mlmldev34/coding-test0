a,b=map(int,input().split())
k,x=map(int,input().split())
t=0
for i in range(a,b+1):
    if abs(i-k)<=x:
        t+=1
if t==0:
    print('IMPOSSIBLE')
else:
    print(t)