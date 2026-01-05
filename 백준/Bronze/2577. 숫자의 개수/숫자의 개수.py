r,n=list([0]*10),[int(input()) for _ in range(3)]
for k in list(str(n[0]*n[1]*n[2])):
  for j in range(10):
    if k==str(j):
      r[j]+=1
for i in r:print(i)