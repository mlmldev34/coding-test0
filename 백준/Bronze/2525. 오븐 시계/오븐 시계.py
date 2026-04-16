h,m=map(int,input().split())
p=int(input())
r=h*60+m+p
if r//60>23:
  print((r//60)%24,end=' ')
else:
  print(r//60,end=' ')
print(r%60)