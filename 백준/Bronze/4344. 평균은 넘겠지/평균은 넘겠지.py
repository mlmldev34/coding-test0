n=int(input())
for k in range(n):
  a=list(map(int,input().split()))
  s=sum(a[1:])/a[0]
  m=0
  for j in a[1:]:
    if j>s:
      m+=1
  print(str(100*m/a[0])+'%')