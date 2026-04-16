n,m=map(int,input().split())
p=[0]*n
for k in range(m):
  i,j,k=map(int,input().split())
  for e in range(i-1,j):
    p[e]=k
[print(i,end=' ') for i in p]