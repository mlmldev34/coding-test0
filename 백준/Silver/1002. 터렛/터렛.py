n=int(input())
for _ in range(n):
  x1,y1,r1,x2,y2,r2=map(int, input().split())
  if(x1==x2 and y1==y2):
    if r1==r2:
      print(-1)
    else:
      print(0)
  else:
    r=((x2-x1)**2+(y2-y1)**2)**0.5
    if r1+r2==r or abs(r2-r1)==r:
      print(1)
    elif min(r1,r2)==r and r1!=r2:
      if max(r1,r2)==r*2:
        print(1)
      elif abs(r2-r1)<r:
        print(2)
      else:
        print(0)
    elif max(r1,r2)<r:
      if r1+r2>r:
        print(2)
      else:
        print(0)
    elif min(r1,r2)>r:
      if r1+r2<r:
        print(0)
      elif abs(r2-r1)<r:
        print(2)
      else:
        print(0)
    elif max(r1,r2)==r:
      print(2)
    elif min(r1,r2)<r and r<max(r1,r2) and r>abs(r2-r1):
      print(2)
    else:
      print(0)