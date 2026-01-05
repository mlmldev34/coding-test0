import sys;n=int(input())
for i in range(n):
  a=sys.stdin.readline().rstrip()
  f=a.index(' ')
  print(int(a[0:f])+int(a[f+1:]))