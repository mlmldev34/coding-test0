n,k=map(int,input().split())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append([x,y])
a=list(input())
x,y=0,0
for i in a:
    if i=='L':
        if not([x-1,y] in arr):
            x-=1
    if i=='R':
        if not([x+1,y] in arr):
            x+=1
    if i=='U':
        if not([x,y+1] in arr):
            y+=1
    if i=='D':
        if not([x,y-1] in arr):
            y-=1
print(x,y)