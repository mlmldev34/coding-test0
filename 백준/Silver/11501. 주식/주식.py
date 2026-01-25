import sys

input = sys.stdin.readline
t=int(input().strip())
for i in range(t):
    n=int(input().strip())
    arr=list(map(int,input().strip().split()))
    arr.reverse()
    sum=0
    temp=arr[0]
    for i in range(1, len(arr)):
        if temp>=arr[i]:
            sum+=temp-arr[i]
        else:
            temp=arr[i]
    print(sum)