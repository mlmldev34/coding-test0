n,a,b=map(int,input().split())
r=1
while not(a%2==1 and a+1==b) and not(b%2==1 and b+1==a):
    r+=1
    if n<=1:
        r=-1
        break
    if a%2==0:
        a//=2
    else:
        a//=2
        a+=1
    if b%2==0:
        b//=2
    else:
        b//=2
        b+=1
    if n%2==0:
        n//=2
    else:
        n//=2
        n+=1
print(r)