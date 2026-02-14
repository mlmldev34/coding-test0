s=input()
arr=[]
r=0
for i in s:
  if len(arr)==0:
    if i=='(':
      arr.append('(')
    else:
      r+=1
  else:
    if i=='(':
      arr.append('(')
    else:
      arr.pop()
print(len(arr)+r)