n=int(input())
p=[]
for i in range(1,n+1):
  if sum([int(str(i)[k]) for k in range(len(str(i)))])+i==n:
    p.append(i)
    break
if len(p)==0:
  print(0)
else:
  print(p[0])