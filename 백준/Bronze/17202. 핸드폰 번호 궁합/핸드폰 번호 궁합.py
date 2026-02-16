a=input()
b=input()
arr=list(a)
brr=list(b)

for k in range(14):
  temp1=arr
  arr=[]
  for i in range((16-k)//2):
    arr.append((int(temp1[i])+int(brr[i]))%10)
  temp2=brr
  brr=[]
  for i in range((15-k)//2):
    brr.append((int(temp1[i+1])+int(temp2[i]))%10)
print(''.join(list(map(str, arr+brr))))