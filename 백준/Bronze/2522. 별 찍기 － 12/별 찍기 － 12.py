n=int(input())
for k in range(1,n+1):
  print(' '*(n-k)+'*'*k)
for k in range(n-1,0,-1):
  print(' '*(n-k)+'*'*k)