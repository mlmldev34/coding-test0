n=int(input())
arr=list(map(int, input().split()))
DP=[0]*(n)
Max=0
answer=1
for i in range(n):
    for j in range(i):
        if(arr[j]<arr[i]):
            Max = max(Max, DP[j])
    DP[i]=Max+1
    if DP[i]>answer:
        answer = DP[i]
    Max=0
print(answer)