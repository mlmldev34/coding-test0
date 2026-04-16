n=int(input())
a=list(map(int,input().split()))
r=0
for i in range(n):
  r+=a[i]
  if i<n-1:
    r+=8
print(r//24,r%24)