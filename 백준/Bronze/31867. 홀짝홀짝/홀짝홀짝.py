n=int(input())
a=list(map(int, input()))
s=sum([i%2 for i in a])
if s>n-s:
    print(1)
elif s<n-s:
    print(0)
else:
    print(-1)