n=[]
s=[]
m=[
['A+',	4.5],
['A0',	4.0],
['B+',	3.5],
['B0',	3.0],
['C+',	2.5],
['C0',	2.0],
['D+',	1.5],
['D0',	1.0],
['F',	0.0]]
for i in range(20):
  a=input().split()
  b=0.0
  for k in m:
    if a[2]==k[0]:
      b=k[1]
      s.append(float(a[1]))
      break
    else:
      b=5.0
  if b!=5.0:
    n.append(b*float(a[1]))
print(sum(n)/sum(s))