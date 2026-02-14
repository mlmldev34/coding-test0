n=int(input())
for _ in range(n):
  s=input()
  result='YES'
  arr=[]
  for i in s:
    if len(arr)==0:
      if i=='(':
        arr.append(i)
      else:
        result='NO'
        break
    else:
      if i=='(':
        arr.append(i)
      else:
        arr.pop()
  if result=='NO':
    print(result)
  else:
    if len(arr)>0:
      print('NO')
    else:
      print(result)