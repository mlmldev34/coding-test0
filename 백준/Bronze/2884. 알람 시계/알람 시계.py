a,b=map(int,input().split())
r=a*60+b-45
if r//60<0:
  print(24+r//69,r%60)
else:
  print(r//60,r%60)