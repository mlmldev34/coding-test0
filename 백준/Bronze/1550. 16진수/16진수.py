a=list(input())
r=0
for i in range(len(a)):
  a[i]=a[i].replace('A','10').replace('B','11').replace('C','12').replace('D','13').replace('E','14').replace('F','15')
for i in range(len(a)):
  r+=int(a[i])*16**(len(a)-1-i)
print(r)