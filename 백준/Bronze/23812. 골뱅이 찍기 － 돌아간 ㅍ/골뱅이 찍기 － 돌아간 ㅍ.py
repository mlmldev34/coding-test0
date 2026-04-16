n=int(input())

for k in range(n*5):

  if (k//n)%2==0:

    print('@'*n+' '*(n*5-2*n)+'@'*n)

  else:

    print('@'*n*5)