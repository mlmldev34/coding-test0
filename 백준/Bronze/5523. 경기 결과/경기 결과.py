import sys

input = sys.stdin.readline

n=int(input().strip())
r1=0
r2=0
for _ in range(n):
    a,b=map(int,input().strip().split())
    r1+=int(a>b)
    r2+=int(b>a)
print(r1,r2)