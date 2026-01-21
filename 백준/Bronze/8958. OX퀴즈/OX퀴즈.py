n=int(input())
for i in range(n):
  a=input()
  r=0
  s=0
  for k in list(a):
    if k=='O':
      s+=1
      r+=s
    else:
      s=0
  print(r)