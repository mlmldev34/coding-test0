n,m=map(int, input().split())
A=1000
B=1000
c=0
for i in range(m):
    a,b=map(int, input().split())
    if A>a:
        A=a
    if B>b:
        B=b
    
if A<B*6:
    if A*(n//6+1)<A*(n//6)+B*(n%6):
        c+=A*(n//6+1)
        n=0
    else:
        c+=A*(n//6)
        n-=(n//6)*6
c+=B*n
print(c)