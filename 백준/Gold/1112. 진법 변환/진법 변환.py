def f(x,b):
  if b>0:
    if x<0:
      x0=abs(x)
    elif x>0:
      x0=x
    else:
      return [0]
  else:
    if x==0:
      return [0]
    else:
      x0=x
  s=x0
  p=[]
  while True:
    if s==0:
      break
    s0=0
    if b<0:
      if s/b<=0 or s%b==0:
        s0=int(s/b)
      else:
        s0=int(s/b)+1
    else:
      s0=s//b
    p.append(s-s0*b)
    s=s0
  for i in range(len(p)):
    if p[i]>abs(b)-1:
      if i<=len(p):
        p[i]=0
        p[i+1]=p[i+1]-1
    elif p[i]<0:
      if i<len(p)-1:
        p[i]=0
        p[i+1]=p[i+1]+1
    elif p[i]==0 and i==len(p)-1:
      p[i]=p[i]+1
  if b>0 and x<0:
    return ['-']+list(map(int,list(reversed(p))))
  else:
    return list(map(int,list(reversed(p))))
x,b=map(int,input().split())
r=f(x,b)
[print(i,end='') for i in r]