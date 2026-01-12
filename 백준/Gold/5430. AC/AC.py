import sys
from collections import deque

input=sys.stdin.readline

n=int(input().strip())

for i in range(n):
    d=1
    s=input().strip()
    m=int(input().strip())
    a=deque(input().strip()[1:-1].split(','))
    if(m==0):
        arr=[]
    queue=a
    for k in s:
        if k=='R':
            d*=-1
        else:
            if m == 0:
                d=2
                break
            if d==1:
                queue.popleft()
                m-=1
            elif d==-1:
                queue.pop()
                m-=1
    if d==2:
        print('error')
    elif d==-1:
        print('['+','.join(list(queue)[::-1])+']')
    elif d==1:
        print('['+','.join(queue)+']')