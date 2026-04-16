a=[]
s=[]
for i in range(5):
  a.append(input())
for i in range(5):
  p=['']*max([len(i) for i in a])
  for j in range(len(a[i])): 
    p[j]=a[i][j]
  s.append(p)
for i in range(len(s[0])):
  for j in range(5):
    if s[j][i]!="":
      print(s[j][i],end='')