n=int(input())
for k in range(1,n+1):
  print('*'*k+' '*(n*2-2*(k-1)-2)+'*'*k)
for k in range(n-1,0,-1):
  print('*'*k+' '*(n*2-2*(k-1)-2)+'*'*k)