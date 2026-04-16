import math

n=int(input())

e=int(math.log10(n)//math.log10(3))

def f(x,i,j):

  for u in range(1,e+1):

    q=i//(3**u)-1

    w=j//(3**u)-1

    if q==e//2+1 and w==e//2+1:

      return 0

    if (q==0 or q%3==0) and (w==0 or w%3==0):

        return 0

  else:

    i=i%3

    j=j%3

    return x[i][j]

p=[[1,1,1],[1,0,1],[1,1,1]]

if n==3:

  print('***')

  print('* *')

  print('***')

else:

  i=0

  j=0

  for k in range(n*n):

    if f(p,i,j):

      print('*',end='')

    else:

      print(' ',end='')

    if (k+1)%(n)==0:

      i+=1

      j+=1

      print()

    else:

      j+=1