n=[]
for k in range(9):
  n.append(int(input()))
r=[]
s=sum(n)-100
for j in n:
  for k in n:
    if j!=k:
      if j+k==s:
        r.append(j)
        r.append(k)
for k in range(9):
  if not(n[k] in r):
    print(n[k])