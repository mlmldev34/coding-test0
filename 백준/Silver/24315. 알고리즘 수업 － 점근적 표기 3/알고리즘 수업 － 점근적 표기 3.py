a1,a0=map(int,input().split())
c1,c2=map(int,input().split())
n0 = int(input())

if (a1-c1)*n0>=-a0 and (a1-c2)*(n0)<=-a0:
    print(1)
else:
    print(0)