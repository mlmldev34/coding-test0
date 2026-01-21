n,b=input().split();n,b=int(n),int(b);
a=[]
for i in range(1, b+1):
  for j in range(i):
    a.append(i)
print(sum(a[n-1:b]))