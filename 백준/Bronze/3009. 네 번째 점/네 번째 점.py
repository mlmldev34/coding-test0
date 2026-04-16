ax,ay=map(int,input().split())
bx,by=map(int,input().split())
cx,cy=map(int,input().split())
p=[]
if ax==bx:
  p.append(cx)
elif ax==cx:
  p.append(bx)
else:
  p.append(ax)
if ay==by:
  p.append(cy)
elif ay==cy:
  p.append(by)
else:
  p.append(ay)
print(p[0],p[1])