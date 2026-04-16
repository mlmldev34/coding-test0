n=int(input())
a=[input().split() for i in range(n)]
for i in a:
  n-=1
  for j in i[1]:
    print(j*int(i[0]), end='')
  if n!=0:
    print()