n,m=map(int,input().split())
a=[]
b=[]
for k in range(n):
  a.append(input())
for k in range(m):
  b.append(input())
c=0
for k in b:
  if k in a:
    c+=1
print(c)