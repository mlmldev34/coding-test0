n=int(input())
for k in range(n,0,-1):
  print(' '*(n-k)+'*'*(k*2-1))
for k in range(2, n+1):
  print(' '*(n-k)+'*'*(k*2-1))