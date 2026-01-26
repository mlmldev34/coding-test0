n=int(input())
arr=list(map(int, input().split()))
arr=list(sorted(arr, reverse=True))
s=0
for i in range(n-1,-1,-1):
    s+=arr[i]*(i+1)
print(s)