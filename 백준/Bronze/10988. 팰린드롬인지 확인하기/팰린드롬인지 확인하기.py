a=input()
l=len(a)
if str(a[0:l//2])==''.join(list(reversed(a[l//2+l%2:]))):
  print(1)
else:
  print(0)