a,b,c=map(int,input().split())
m=max(a,b,c)
s=a+b+c
if 2*m<s:
    print(s)
else:
    print(2*s-2*m-1)