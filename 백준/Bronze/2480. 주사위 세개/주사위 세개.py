a=sorted(list(map(int,input().split())))
if a.count(a[0])==3:
  print(10000+a[0]*1000)
elif a.count(a[0])==2:
  print(1000+a[0]*100)
elif a.count(a[1])==2:
  print(1000+a[1]*100)
else:
  print(a[2]*100)