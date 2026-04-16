n=int(input())
s=[]
for k in range(n):
  a=list(map(int,input().split()))
  a0=a[0:2]
  a1=a[2:]
  s.append(max(a0)+sum(list(sorted(a1,reverse=True))[0:2]))
print(max(s))