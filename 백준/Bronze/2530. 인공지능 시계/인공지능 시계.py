h,m,s=map(int,input().split())
s0=int(input())
s1=h*60*60+m*60+s+s0
hp=s1//(60*60)
mp=s1//60
mp=mp-hp*60
sp=s1%60
if s1>=24*60:
  hp=hp%24
print(hp,mp,sp)