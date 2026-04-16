def func(n):
  if (n%4==0 and n%100!=0) or n%400==0:
    return 1
  else:
    return 0
p=[31,28,31,30,31,30,31,31,30,31,30,31]
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
n1,n2a,n2b,n3a,n3b=0,0,0,a1[2],a2[2]
for i in range(a1[0],a2[0]):
  n1+=365+func(i)
if a1[1]!=1:
  for i in range(a1[1]-1):
    if i==1:
      n2a+=(p[i]+func(a1[0]))
    else:
      n2a+=p[i]
else:
  n2a=0
if a2[1]!=1:
  for i in range(a2[1]-1):
    if i==1:
      n2b+=(p[i]+func(a2[0]))
    else:
      n2b+=p[i]
else:
  n2b=0
if (a2[0]-a1[0]==1000 and (n2b+n3b)-(n2a+n3a)>=0) or a2[0]-a1[0]>1000:
  print('gg')
else:
  print('D-',end='')
  print(n1-(n2a+n3a)+(n2b+n3b))