a=[[]]*9
for i in range(9):
  a[i]=list(map(int,input().split()))
b=[]
for i in range(9):
  b.append(list(sorted(a[i]))[-1])
r=list(sorted(b))[-1]
print(r)
m=[]
for i in range(9):
  if r in a[i]:
    m.append(i)
    break
m.append(a[m[0]].index(r))
print(m[0]+1,m[1]+1)