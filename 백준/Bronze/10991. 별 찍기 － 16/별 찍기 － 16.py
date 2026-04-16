n=int(input())+1
for k in range(1,n):
  if k==1:
    print(' '*(n-k-1)+'*')
  else:
    print(' '*(n-k-1),end='')
    for j in range(1,k+1):
      print('*',end=' ')
    print()