n,a=input(),[]
for i in range(1,2**(len(n))+1):
  k=bin(i)[2:].replace('0','7').replace('1','4')
  k2=bin(i)[2:].replace('0','4').replace('1','7')
  if int(k)<=int(n):
    a.append(int(k))
  if int(k2)<=int(n):
    a.append(int(k2))
print(max(a))