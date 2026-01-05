a=input().upper()
s='abcdefghijklmnopqrstuvwxyz'.upper()
d=[]
for k in s:
  d.append(a.count(k))
x=max(d)
if d.count(x)>=2:
  print('?')
else:
  print(s[d.index(max(d))])