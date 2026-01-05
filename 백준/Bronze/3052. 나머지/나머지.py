n=[i%42 for i in [int(input()) for _ in range(10)]];r=[None]*10;x=10
for k in range(10):
  for j in range(10):
    if n[k]==n[j]:
      if not(n[j] in r):
        r[k]=n[j]
        break
for i in range(10):
  if r[i]==None:
    x-=1
print(x)