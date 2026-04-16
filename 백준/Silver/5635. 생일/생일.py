n=int(input())
a=[]
b=[]
y=[['','','']]*n
for i in range(n):
  d=input().split()
  a.append(d)
  b.append(d)
for i in range(n):
  y[i][0]=a[i][3]
  if len(a[i][2])==1:
    y[i][1]='0'+a[i][2]
  else:
    y[i][1]=a[i][2]
  if len(a[i][1])==1:
    y[i][2]='0'+a[i][1]
  else:
    y[i][2]=a[i][1]
  a[i]=''.join(y[i])
print(b[a.index(list(sorted(a))[-1])][0])
print(b[a.index(list(sorted(a))[0])][0])