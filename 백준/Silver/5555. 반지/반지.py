s=input()
n=int(input())
r=0
for _ in range(n):
  a=input()
  if s in a*2:
    r+=1
print(r)