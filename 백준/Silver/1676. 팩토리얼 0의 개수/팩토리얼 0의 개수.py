n=int(input())
r=1;s=0
for i in range(1,n+1):
  r*=i
for i in list(reversed(str(r))):
  if i=='0':
    s+=1
  else:
    break
print(s)