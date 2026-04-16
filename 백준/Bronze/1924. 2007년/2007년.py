x,y=map(int,input().split())
m=[31,28,31,30,31,30,31,31,30,31,30,31]
d=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
p=0
if x>1:
  for k in range(x-1):
    p+=m[k]
if p+y<=7:
  print(d[(p+y)-1])
else:
  print(d[(p+y)%7-1])