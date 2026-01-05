a=input()
l=len(a)
for k in range(l//10):
  print(a[0+10*k:10*(k+1)])
if l%10>0:
  print(a[10*(l//10):])