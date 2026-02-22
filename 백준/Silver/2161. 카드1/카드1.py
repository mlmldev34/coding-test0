n=int(input())
arr=list(range(1,n+1))
brr=[]
for i in range(n*2-1):
  if i%2:
    temp=arr[0]
    arr.pop(0)
    arr.append(temp)
  else:
    brr.append(arr.pop(0))
print(' '.join(list(map(str,brr))))