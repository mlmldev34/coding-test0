s=input()
a='abcdefghijklmnopqrstuvwxyz'
for k in list(a):
  if s.count(k)>0:
    print(s.index(k), end=' ')
  else:
    print(-1, end=' ')