import sys

input = sys.stdin.readline

for i in range(3):
    n=int(input().strip())
    s=0
    for _ in range(n):
        s+=int(input().strip())
    if s==0:
        print(0)
    elif s>0:
        print('+')
    else:
        print('-')