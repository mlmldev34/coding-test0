a=input()
r=[0,0]
for i in range(len(a)):
  if i+3<=len(a):
    if ''.join(a[i:i+3])=='JOI':
      r[0]+=1
    if ''.join(a[i:i+3])=='IOI':
      r[1]+=1
print(r[0])
print(r[1])