o=int(input())
for k in range(o):
  h,w,n=map(int,input().split())
  if n%h==0:
    if n//h<=9:
      print(str(h)+'0'+str(n//h))
    else:
      print(str(h)+str(n//h))
  else:
    if n//h<=8:
      print(str(n%h)+'0'+str(n//h+1))
    else:
      print(str(n%h)+str(n//h+1))