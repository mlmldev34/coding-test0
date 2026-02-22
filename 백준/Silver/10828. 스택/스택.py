import sys

input = sys.stdin.readline

n=int(input().strip())
arr=[]
for _ in range(n):
  a,*n=input().strip().split()
  if a=='push':
    arr.append(int(n[0]))
  elif a=='pop':
    print(arr.pop(-1) if len(arr)!=0 else -1)
  elif a=='top':
    print(arr[-1] if len(arr)!=0 else -1)
  elif a=='empty':
    print(1 if len(arr)==0 else 0)
  else:
    print(len(arr))