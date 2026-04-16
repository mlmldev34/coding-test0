n=input()
s=n
i=0
if int(n)<10:
  n=n+'0'
  s=n
while True:
  if int(n)<10:
    n=n+'0'
  a=int(n[0])+int(n[1])
  n=n[1]+str(a)[-1]
  if n==s:
    print(i+1)
    break
  i+=1
if(n!=s):
  print(1)