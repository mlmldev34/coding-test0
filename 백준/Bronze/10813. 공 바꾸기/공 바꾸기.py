n,m=map(int,input().split())
p=[i+1 for i in range(n)]
for k in range(m):
  i,j=map(int,input().split())
  l=p[i-1]
  p[i-1]=p[j-1]
  p[j-1]=l
[print(i,end=' ') for i in p]