def func(n):
  if (n%4==0 and n%100!=0) or n%400==0:
    return 1
  else:
    return 0

mo=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
m1=[31,28,31,30,31,30,31,31,30,31,30,31]
a=input().split(',')
m=a[0].split()[0]
d=int(a[0].split()[1])
y=int(a[1].split()[0])
t=a[1].split()[1]
for i in mo:
  if m==i:
    m=mo.index(i)+1
    break
y0=365+func(y)
mp=0
for i in range(m-1):
  if i==1:
    mp+=m1[i]+func(y)
  else:
    mp+=m1[i]
tp=(int(t.split(':')[0])+int(t.split(':')[1])/60)/24
print(((mp+d-1+tp)/y0)*100)