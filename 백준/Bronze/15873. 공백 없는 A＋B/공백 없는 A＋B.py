s=input()
l=len(s)
a=''
b=''

if l>2:
  if l==3:
    a='10'
    b=s.replace('10','')
    print(int(a)+int(b))
  else:
    print(20)
else:
  print(int(s[0])+int(s[1]))  