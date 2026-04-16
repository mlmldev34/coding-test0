r,n=0,int(input())
a=list(map(int, input().split()))
if max(a)%2==0:
  print(max(a)*2)
else:
  print(max(a)*min(a))