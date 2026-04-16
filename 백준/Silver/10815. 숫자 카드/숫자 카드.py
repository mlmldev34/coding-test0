n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=set(b)&set(a)
for k in range(m):
  print(int(b[k] in c),end=' ')