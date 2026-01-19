while True:
  a=input()
  if a.split()[0]+a.split()[1]=='00':
   break
  print(sum(map(int,a.split())))