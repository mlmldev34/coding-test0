a,b,c,d,e,f=map(int,input().split())
for x in range(-999,1000):
  for y in range(-999,1000):
    if x*a+b*y==c and x*d+y*e==f:
      print(x,y)
      break