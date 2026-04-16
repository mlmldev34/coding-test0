def fact(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(fact(b)//(fact(b-a)*fact(a)))