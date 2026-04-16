a=input()

l=0

r=[]

if len(a)%3>0:

  l=len(a)//3

  r.append(a[0:len(a)%3])

  for i in range(l):

    r.append(a[len(a)%3+i*3:len(a)%3+i*3+3])

else:

  l=len(a)//3

  for i in range(l):

    r.append(a[i*3:i*3+3])

s=''

for k in r:

  if len(k)<3:

    k='0'*(3-len(k))+k

    s=s+str(int(k[0])*(2**2)+int(k[1])*(2**1)+int(k[2])*(2**0))

  else:

    s=s+str(int(k[0])*(2**2)+int(k[1])*(2**1)+int(k[2])*(2**0))

print(s)