a=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b=list(input())
r=0
for k in range(8):
  for j in b:
    if j in list(a[k]):
      r+=3+k
print(r)