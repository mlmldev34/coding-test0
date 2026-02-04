import sys
input=sys.stdin.readline

n=int(input().strip())
arr=list(map(int,input().strip().split()))
arr.sort()
x=int(input().strip())
start,end=0,n-1
cnt=0

while start<end:
    if arr[start] + arr[end] == x:
        cnt+=1
        start+=1
        end-=1
    elif arr[start] + arr[end] > x:
        end-=1
    elif arr[start] + arr[end] < x:
        start+=1

print(cnt)