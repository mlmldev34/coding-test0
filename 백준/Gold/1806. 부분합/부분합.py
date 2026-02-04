import sys

input = sys.stdin.readline

N,S=map(int,input().strip().split())
arr=list(map(int, input().strip().split()))

end=0
interval_sum=0

min=N+1

for start in range(N):
    while interval_sum < S and end < N:
        interval_sum += arr[end]
        end += 1
    if interval_sum >= S:
        if min > end-start:
            min=end-start
    interval_sum -= arr[start]

print(min if min<N+1 else 0)