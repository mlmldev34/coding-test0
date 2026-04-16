n,m=map(int,input().split())
p=[i+1 for i in range(n)]
for k in range(m):
  i,j=map(int,input().split())
  l=list(reversed(p[i-1:j]))
  for e in range(i-1,j):
    p[e]=l[e-i+1]
[print(i,end=' ') for i in p]