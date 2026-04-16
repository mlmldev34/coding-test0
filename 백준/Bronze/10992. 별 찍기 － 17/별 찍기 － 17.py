n=int(input())+1
for k in range(1,n):
  if k==1:
    print(' '*(n-k-1)+'*')
  elif k==n-1:
    print('*'*(2*(n-1)-1))
  else:
    print(' '*(n-k-1),end='')
    print('*',end='')
    for j in range(1,k):
      print(' ',end='')
    print(' '*(k-2)+'*')