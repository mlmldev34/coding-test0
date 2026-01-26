n=int(input())
a=[]
for k in range(n):
  a.append(list(map(int,input().split())))
x=[k[0] for k in a]
y=[k[1] for k in a]
mx=max(x)-min(x)
my=max(y)-min(y)
print(mx*my)