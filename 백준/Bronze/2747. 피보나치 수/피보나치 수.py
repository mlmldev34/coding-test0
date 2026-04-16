n=int(input())
k=0
i=1
a=[]
for _ in range(n//2+1):
  a.append(k)
  k=k+i
  a.append(i)
  i=k+i
print(a[n])